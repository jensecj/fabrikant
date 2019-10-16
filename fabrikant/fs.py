from .util import set_runner


@set_runner
def exists(c, runner, path):
    """
    Return True if `path' exists.
    """
    cmd = "test -e '{}'".format(path)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def touch(c, runner, file):
    """
    Return True if touching `file' succeeds.
    """
    cmd = "touch {}".format(file)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def is_file(c, runner, path):
    """
    Return True if `path' is a file.
    """
    cmd = "test -f {}".format(path)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def is_directory(c, runner, path):
    """
    Return True if `path' is a directory.
    """
    cmd = "test -d {}".format(path)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def is_symlink(c, runner, path):
    """
    Return True if `path' is a symbolic link.
    """
    cmd = "test -h {}".format(path)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def is_socket(c, runner, path):
    """
    Return True if `path' is a UNIX socket.
    """
    cmd = "test -S {}".format(path)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def is_readable(c, runner, path):
    """
    Return True if `path' has the readable bit set.
    """
    cmd = "test -r {}".format(path)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def is_writable(c, runner, path):
    """
    Return True if `path' has the writable bit set.
    """
    cmd = "test -w {}".format(path)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def is_executable(c, runner, path):
    """
    Return True if `path' has the executable bit set.
    """
    cmd = "test -x {}".format(path)
    return runner(cmd, hide=True, warn=True).ok


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


@set_runner
def type(c, runner, path):
    """
    Return which type of file `path' is.
    """
    cmd = "stat --format='%F' {}".format(path)
    owner = runner(cmd, hide=True, warn=True).stdout.strip()
    return owner


@set_runner
def size(c, runner, path):
    """
    Return the size of `path', in bytes.
    """
    cmd = "stat --format='%s' {}".format(path)
    owner = runner(cmd, hide=True, warn=True).stdout.strip()
    return owner


@set_runner
def time_of_birth(c, runner, path):
    """
    Return the time when `path' was created.
    """
    cmd = "stat --format='%w' {}".format(path)
    owner = runner(cmd, hide=True, warn=True).stdout.strip()
    return owner


@set_runner
def time_of_last_access(c, runner, path):
    """
    Return the last time `path' was accessed.
    """
    cmd = "stat --format='%x' {}".format(path)
    owner = runner(cmd, hide=True, warn=True).stdout.strip()
    return owner


@set_runner
def time_of_last_change(c, runner, path):
    """
    Return the last time `path' was changed.
    """
    cmd = "stat --format='%y' {}".format(path)
    owner = runner(cmd, hide=True, warn=True).stdout.strip()
    return owner


@set_runner
def create_directory(c, runner, directory, user=None, group=None, mode=None):
    """
    Return True if creating `directory', and settings its user, group,
    and mode all succeed.
    """
    cmd = "mkdir -p {}".format(directory)
    mkdir = runner(cmd).ok

    chown = True
    chgrp = True
    if user is not None:
        group = group or user
        chown = change_owner(c, directory, user)
        chgrp = change_group(c, directory, group)

    chmod = True
    if mode is not None:
        chmod = change_mode(c, directory, mode)

    return mkdir and chown and chgrp and chmod


@set_runner
def remove_directory(c, runner, directory):
    """
    Return True if removing `directory' succeeds.
    """
    cmd = "rmdir {}".format(directory)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def copy(c, runner, source, destination, recursive=False):
    """
    Return True if copying `source' to `destination' succeeds.
    """
    recursive = "-r" if recursive else ""
    cmd = "cp {} {} {}".format(recursive, source, destination)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def move(c, source, destination):
    """
    Return True if moving `source' to `destination' succeeds.
    """
    cmd = "mv {} {}".format(source, destination)
    return runner(cmd, hide=True, warn=True).ok


@set_runner
def remove(c, runner, path, recursive=False):
    """
    Return True if removing `path' succeeds.
    """
    recursive = "-r" if recursive else ""
    cmd = "rm {} {}".format(recursive, path)
    return runner(cmd, hide=True, warn=True).ok