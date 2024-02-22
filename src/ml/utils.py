import time


def time_elapsed(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"TIME_TAKEN: {func.__name__} {(end-start)*10**3:.03f}ms")

    return wrapper
