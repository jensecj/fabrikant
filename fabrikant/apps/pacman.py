from ..util import set_runner


@set_runner
def is_installed(c, runner, program):
    """
    Return True if `program' is installed.
    """
    cmd = "pacman-query {}".format(program)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def upgrade(c, runner):
    """
    Return True if upgrading all packages on the system succeeds.
    """
    cmd = "pacman -Syu"
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def install(c, runner, program):
    """
    Return True if installing `program' succeeds.
    """
    cmd = "pacman -S {}".format(program)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def uninstall(c, runner, program):
    """
    Return True if uninstalling `program' succeeds.
    """
    cmd = "pacman -Rs {}".format(program)
    return runner(cmd, hide=True, warn=True).ok
