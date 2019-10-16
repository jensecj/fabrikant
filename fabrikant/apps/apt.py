from ..util import set_runner


@set_runner
def is_installed(c, runner, program):
    """
    Return True if `program' is installed.
    """
    cmd = "dpkg-query -s {}".format(program)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def update(c, runner):
    """
    Return True if updating package repository succeeds.
    """
    cmd = "apt update"
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def upgrade(c, runner):
    """
    Return True if upgrading all packages on the system succeeds.
    """
    cmd = "apt upgrade"
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def install(c, runner, program):
    """
    Return True if installing `program' succeeds.
    """
    cmd = "apt install {}".format(program)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def uninstall(c, runner, program):
    """
    Return True if uninstalling `program' succeeds.
    """
    cmd = "apt remove {}".format(program)
    return runner(cmd, hide=True, warn=True).ok
