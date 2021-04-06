import time
from functools import wraps


def slow_down(func):
    @wraps(func)
    def wrap_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrap_slow_down


@slow_down
def count_down(from_num):
    if from_num < 1:
        print("Liftoff!")
    else:
        print(from_num)
        count_down(from_num - 1)


if __name__ == "__main__":
    print(count_down(5))
