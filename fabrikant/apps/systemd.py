from ..util import set_runner


@set_runner
def enable(c, runner, service):
    """
    Return True if enabling `service' succeeds.
    """
    cmd = "systemctl enable {}".format(service)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def disable(c, runner, service):
    """
    Return True if disabling `service' succeeds.
    """
    cmd = "systemctl disable {}".format(service)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def start(c, runner, service):
    """
    Return True if starting `service' succeeds.
    """
    cmd = "systemctl start {}".format(service)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def stop(c, runner, service):
    """
    Return True if stopping `service' succeeds.
    """
    cmd = "systemctl stop {}".format(service)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def restart(c, runner, service):
    """
    Return True if restarting `service' succeeds.
    """
    cmd = "systemctl restart {}".format(service)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def reload(c, runner, service):
    """
    Return True if reloading `service' succeeds.
    """
    cmd = "systemctl reload {}".format(service)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def is_active(c, runner, service):
    """
    Return True if `service' is active.
    """
    cmd = "systemctl is-active {}".format(service)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def is_failed(c, runner, service):
    """
    Return True if `service' has failed.
    """
    cmd = "systemctl is-failed {}".format(service)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def show(c, runner, service):
    """
    Return the output of `systemctl show' for `service'.
    """
    cmd = "systemctl show {}".format(service)
    output = runner(cmd, hide=True, warn=True).stdout.strip()
    return output


@set_runner
def status(c, runner, service):
    """
    Return the output of `systemctl status' for `service'.
    """
    cmd = "systemctl status {}".format(service)
    output = runner(cmd, hide=True, warn=True).stdout.strip()
    return output
