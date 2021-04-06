import time
from functools import wraps


def timer(func):
    """
    Print out the runtime of a function
    :param: func
    :return: func
    """

    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


@timer
def lets_waste_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])


if __name__ == "__main__":
    lets_waste_time(10)
