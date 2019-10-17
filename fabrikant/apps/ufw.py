from ..util import set_runner


@set_runner
def enable(c, runner, rule):
    """
    Return True if enabling UFW succeeds.
    """
    cmd = "ufw enable"
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def disable(c, runner, rule):
    """
    Return True if disablind UFW succeeds.
    """
    cmd = "ufw disable"
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def reload(c, runner):
    """
    Return True if reloading UFW succeeds.
    """
    cmd = "ufw reload"
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def allow(c, runner, rule):
    """
    Return True if adding `rule' to UFW succeeds.
    """
    cmd = "ufw allow {}".format(rule)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def deny(c, runner, rule):
    """
    Return True if adding `rule' to UFW succeeds.
    """
    cmd = "ufw deny {}".format(rule)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def limit(c, runner, rule):
    """
    Return True if adding `rule' to UFW succeeds.
    """
    cmd = "ufw limit {}".format(rule)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def delete(c, runner, rule):
    """
    Return True if removing `rule' to UFW succeeds.
    """
    cmd = "ufw delete {}".format(rule)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def status(c, runner, verbose=False):
    """
    Return the status of UFW.
    """
    verbose = "verbose" if verbose else ""
    cmd = "ufw status {}".format(verbose)
    ret = runner(cmd, hide=True, warn=True)
    if ret.ok:
        return ret.stdout.strip()
    else:
        print(ret.stderr.strip())


@set_runner
def enabled(c, runner):
    """
    Return True if UFW is enabled.
    """
    cmd = "ufw status | head -1"
    ret = runner(cmd, hide=True, warn=True)

    if ret.stderr and not ret.ok:
        print(ret.stderr)

    return ret.ok and "Status: active" in ret.stdout
