from typing import Callable


def exclamation(func: Callable[..., str]) -> Callable[..., str]:
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!"

    return wrapper


def add_suffix(suffix: str) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + suffix

        return wrapper

    return decorator
