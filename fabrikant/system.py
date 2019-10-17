from .util import set_runner
from .fs import exists

# * environment


@set_runner
def has_program(c, runner, program):
    """
    Return True if  `program' is in in $PATH.
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
    Return the current user.
    """
    cmd = "whoami"
    user = runner(cmd, hide=True, warn=True).stdout.strip()
    return user


@set_runner
def users_online(c, runner):
    """
    Return all users who are currently logged in.
    """
    cmd = "users"
    users = runner(cmd, hide=True, warn=True).stdout.strip().split()
    return users


@set_runner
def user_exists(c, runner, user):
    """
    Return True if `user' exists.
    """
    cmd = "users"
    users = runner(cmd, hide=True, warn=True).stdout.strip()
    return user in users


@set_runner
def create_user(c, runner, group):
    pass


# * groups


@set_runner
def groups(c, runner):
    """
    Return all groups on the system.
    """
    cmd = "groups"
    groups = runner(cmd, hide=True, warn=True).stdout.strip().split()
    return groups


@set_runner
def group_exists(c, runner, group):
    """
    Return True if `group' exists.
    """
    cmd = "groups"
    groups = runner(cmd, hide=True, warn=True).stdout.strip()
    return group in groups


@set_runner
def create_group(c, runner, group):
    pass
