from .util import set_runner
from .fs import exists

# * environment


@set_runner
def has_program(c, runner, program):
    """
    Return True if `program' is in in $PATH.
    """
    cmd = "which {}".format(program)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def distro(c, runner):
    """
    Return the best guess of the name of the distribution.
    Tries, in order, `lsb_release', looking for sentinal files, and uname.
    """
    if has_program(c, "lsb_release"):
        cmd = "lsb_release --short --id --release --codename"
        distro = runner(cmd, hide=True, warn=True).stdout.replace("\n", " ").strip()
        return distro

    files = {
        "manjaro-release": "manjaro",
        "arch-release": "arch",
        "centos-release": "centos",
        "fedora-release": "fedora",
    }

    for k in files.keys():
        file = os.path.join("/etc/", k)
        if exists(file):
            return files[k]

    cmd = "uname -a"
    distro = runner(cmd, hide=True, warn=True).stdout.strip()

    return distro


@set_runner
def hostname(c, runner):
    """
    Return the hostname of the machine.
    """
    cmd = "hostname"
    hostname = runner(cmd, hide=True, warn=True).stdout.strip()
    return hostname


# * users


@set_runner
def current_user(c, runner):
    """
    Return the name of the current user.
    """
    cmd = "whoami"
    user = runner(cmd, hide=True, warn=True).stdout.strip()
    return user


@set_runner
def users_online(c, runner):
    """
    Return a list of names of all users who are currently logged in.
    """
    cmd = "users"
    users = runner(cmd, hide=True, warn=True).stdout.strip().split()
    return users


@set_runner
def user_exists(c, runner, user):
    """
    Return True if `user' exists.
    """
    cmd = "id -u {}".format(user)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def create_user(c, runner, user, group=None, shell=None):
    """
    Return True if `user' already exists, or creating `user' succeeds.
    """
    if user_exists(c, user, runner=runner):
        return True

    group = "-G {}".format(group) if group else ""
    shell = "-s {}".format(shell) if shell else ""
    cmd = "useradd {} {} {}".format(group, shell, user)
    return runner(cmd, hide=True, warn=True).ok


# * accessors


@set_runner
def groups(c, runner):
    """
    Return a list of all groups on the system.
    """
    cmd = "cat /etc/group | cut -d: -f1"
    groups = runner(cmd, hide=True, warn=True).stdout.strip().split()
    return groups


@set_runner
def user_groups(c, runner, user):
    """
    Return a list of all groups `user' is in.
    Return None if user does not exist.
    """
    if not user_exists(c, user, runner=runner):
        return None

    cmd = "groups {}".format(user)
    output = runner(cmd, hide=True, warn=True)

    if output.ok:
        return output.stdout.strip().split()


# * predicates


@set_runner
def group_exists(c, runner, group):
    """
    Return True if `group' exists.
    """
    return group in groups(c, runner=runner)


@set_runner
def user_in_group(c, runner, user, group):
    """
    Return True if `user' is a member of `group'.
    Return None if either `user' or `group' does not exist.
    """
    if not user_exists(c, user, runner=runner):
        return None

    if not group_exists(c, group, runner=runner):
        return None

    groups = user_groups(c, user, runner=runner)
    return user in groups


# * mutators


@set_runner
def user_add_group(c, runner, user, group):
    """
    Return True if `user' is already a member of `group', or adding `user' to `group' succeeds.
    Return None if either `user' or `group' does not exist.
    """
    if not user_exists(c, user, runner=runner):
        return None

    if not group_exists(c, group, runner=runner):
        return None

    if user_in_group(c, user, group, runner=runner):
        return True

    group = "-G {}".format(group)
    cmd = "usermod {} {}".format(group, user)
    return runner(cmd, hide=True, warn=True).ok


