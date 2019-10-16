from .util import set_runner


@set_runner
def has_program(c, runner, program):
    """
    Return True if  `program' is in in $PATH.
    """
    cmd = "which {}".format(program)
    return runner(cmd, hide=True, warn=True).ok
