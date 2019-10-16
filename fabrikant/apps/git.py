from ..util import set_runner


@set_runner
def latest_commit(c, runner, repo):
    """
    Return a triplet of the latest commits hash, timestamp, and message.
    """
    cmd = "cd {} && git log --format='%H %ai %B' -n 1".format(repo)
    commit = runner(cmd, hide=True, warn=True).stdout.strip().split()
    id = commit[0]
    timestamp = " ".join(commit[1:4])
    msg = " ".join(commit[4:])
    return id, timestamp, msg


@set_runner
def latest_commit_hash(c, runner, repo):
    """
    Return the hash of the latest commit.
    """
    id, _, _ = latest_commit(c, repo, runner=runner)
    return id


@set_runner
def latest_commit_timestamp(c, runner, repo):
    """
    Return the timestamp of the latest commit.
    """
    _, timestamp, _ = latest_commit(c, repo, runner=runner)
    return timestamp


@set_runner
def latest_commit_message(c, runner, repo):
    """
    Return the message of the latest commit.
    """
    _, _, msg = latest_commit(c, repo, runner=runner)
    return msg
