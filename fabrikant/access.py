from .util import set_runner
from .fs import exists
from .system import user_exists, group_exists

# * accessors


@set_runner
def owner_name(c, runner, path):
    """
    Return the name of the owner of `path'.
    """
    cmd = "stat --format='%U' {}".format(path)
    owner = runner(cmd, hide=True, warn=True).stdout.strip()
    return owner


@set_runner
def owner_group(c, runner, path):
    """
    Return the group-name of the owner of `path'.
    """
    cmd = "stat --format='%G' {}".format(path)
    owner = runner(cmd, hide=True, warn=True).stdout.strip()
    return owner


# * mutators


@set_runner
def change_owner(c, runner, path, user, recursive=False):
    """
    Return True if `path' is already owned by `user', or if setting owner to `user' succeeds.
    Return None if either `path' or `user' does not exist.
    """
    if not exists(c, path, runner=runner):
        return None

    if not user_exists(c, user, runner=runner):
        return None

    # it is very expensive to know for sure if we own all files in a
    # path recursively, so we just assume we dont
    if not recursive and owner_name(c, path, runner=runner) == user:
        return True

    recursive = "-R" if recursive else ""
    cmd = "chown {} {} {}".format(recursive, user, path)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def change_group(c, runner, path, group, recursive=False):
    """
    Return True if `path' is already owned by `group', or if setting owner to `group' succeeds.
    Return None if either `path' or `group' does not exist.
    """
    if not exists(c, path, runner=runner):
        return None

    if not group_exists(c, group, runner=runner):
        return None

    # it is very expensive to know for sure if we own all files in a
    # path recursively, so we just assume we dont
    if not recursive and owner_group(c, path, runner=runner) == group:
        return True

    recursive = "-R" if recursive else ""
    cmd = "chgrp {} {} {}".format(recursive, group, path)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def change_mode(c, runner, path, mode, recursive=False):
    """
    Return True if `path' is already owned by `user', or if setting owner to `user' succeeds.
    Return None if `path' does not exist.
    """
    if not exists(c, path, runner=runner):
        return None

    # TODO: validate mode
    recursive = "-R" if recursive else ""
    cmd = "chmod {} {} {}".format(recursive, mode, path)
    return runner(cmd, hide=True, warn=True).ok
