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


@set_runner
def branch(c, runner, repo):
    """
    Return the name of the current branch.
    """
    cmd = "cd {} && git rev-parse --abbrev-ref HEAD".format(repo)
    output = runner(cmd, hide=True, warn=True)

    if output.ok:
        return output.stdout.strip()


@set_runner
def is_clean(c, runner, repo):
    """
    Return True if `repo' is clean (has no uncommitted changes).
    """
    cmd = "cd {} && git diff --quiet".format(repo)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def is_dirty(c, runner, repo):
    """
    Return True if `repo' is dirty (has uncommitted changes).
    """
    return not is_clean(c, repo, runner=runner)

