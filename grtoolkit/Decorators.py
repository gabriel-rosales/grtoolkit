import functools, time

def try_pass(func):
    """Try/except/pass runtime of decorated function"""

    @functools.wraps(func)
    def wrapper_try_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            pass

    return wrapper_try_func


def timer(func):
    """Print runtime of decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


def debug(func):
    """Print the function signature and return value, useful for when a program is run multiple times.
    Example: Factorials"""

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        # Do something before
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        # Do something after
        print(f"{func.__name__!r} returned {value!r}")
        return value

    return wrapper_debug


def slow_down(func, sec=1):
    """Sleep 1 second before calling function"""

    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(sec)
        return func(*args, **kwargs)

    return wrapper_slow_down


class wait(object):
    """Decorator to wait a specified number of seconds.
    Usage: @wait(seconds)"""

    # ref: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html
    def __init__(self, sec):
        self.sec = sec

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper_wait(*args, **kwargs):
            time.sleep(self.sec)
            return func(*args, **kwargs)

        return wrapper_wait

if __name__ == "__main__":
    pass
    