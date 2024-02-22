import functools
import time


def time_elapsed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"TIME_TAKEN: {func.__name__} {(end-start)*10**3:.03f}ms")
        return func(*args, **kwargs)

    return wrapper
