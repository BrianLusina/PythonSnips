from typing import Callable, Union
from types import FunctionType


def add(n: int) -> Union[Callable, FunctionType]:
    def wrapper(x: int):
        return n + x

    return wrapper
