from ..util import set_runner


# * accessors


@set_runner
def running_units(c, runner):
    """
    Return a list of all running units.
    """
    cmd = "systemctl list-units --no-pager --no-legend --state=running | cut -d' ' -f1"
    units = runner(cmd, hide=True, warn=True).stdout.strip().split()
    return units


@set_runner
def active_units(c, runner):
    """
    Return a list of all active units.
    """
    cmd = "systemctl list-units --no-pager --no-legend --state=active | cut -d' ' -f1"
    units = runner(cmd, hide=True, warn=True).stdout.strip().split()
    return units


@set_runner
def failed_units(c, runner):
    """
    Return a list of all failed units.
    """
    cmd = "systemctl list-units --no-pager --no-legend --state=failed | cut -d' ' -f1"
    units = runner(cmd, hide=True, warn=True).stdout.strip().split()
    return units


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


# * predicates


@set_runner
def is_active(c, runner, service):
    """
    Return True if `service' is active.
    """
    cmd = "systemctl is-active {}".format(service)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def is_enabled(c, runner, unit):
    """
    Return True if `unit' is enabled.
    """
    cmd = "systemctl is-enabled {}".format(unit)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def is_failed(c, runner, service):
    """
    Return True if `service' has failed.
    """
    cmd = "systemctl is-failed {}".format(service)
    return runner(cmd, hide=True, warn=True).ok


# * mutators


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
