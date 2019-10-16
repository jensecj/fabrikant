from functools import wraps


def set_runner(f):
    """
    Set the second posarg of `f' to an appropriate runner for the context.
    The first arg of `f' is expected to be an `~Invoke.context.Context'.

    The runner can be set directly using the kwarg `runner'.
    By default, the runner is the `run' method of the context,
    if kwarg `sudo' is set, the runner will be the `sudo' method of the context.
    """

    @wraps(f)
    def inner(*args, **kwargs):
        args = list(args)
        context = args[0]

        runner = kwargs.pop("runner", None)
        sudo = kwargs.pop("sudo", False)

        if not runner:
            method = "sudo" if sudo else "run"
            runner = getattr(context, method)

        args.insert(1, runner)
        return f(*args, **kwargs)

    return inner
