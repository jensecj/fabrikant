from ..util import set_runner


@set_runner
def latest_commit_hash(c, runner, repo):
    """
    Return the hash of the latest commit.
    """
    cmd = "cd {} && git log --format='%H' -n 1".format(repo)
    ret = runner(cmd, hide=True, warn=True)
    if ret.ok:
        return ret.stdout.strip()


@set_runner
def latest_commit_timestamp(c, runner, repo):
    """
    Return the timestamp of the latest commit.
    """
    cmd = "cd {} && git log --format='%ai' -n 1".format(repo)
    ret = runner(cmd, hide=True, warn=True)
    if ret.ok:
        return ret.stdout.strip()


@set_runner
def latest_commit_message(c, runner, repo):
    """
    Return the message of the latest commit.
    """
    cmd = "cd {} && git log --format='%B' -n 1".format(repo)
    ret = runner(cmd, hide=True, warn=True)
    if ret.ok:
        return ret.stdout.strip()

