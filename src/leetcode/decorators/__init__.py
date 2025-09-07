from typing import Callable


def exclamation(func: Callable[..., str]) -> Callable[..., str]:
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!"

    return wrapper
