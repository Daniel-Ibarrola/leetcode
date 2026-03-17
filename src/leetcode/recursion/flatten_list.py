from collections.abc import Generator
from typing import Any
from typing import TypeAlias, TypeVar

T = TypeVar("T")
NestedList: TypeAlias = list[T | "NestedList[T]"]


def flatten_list(list_: list[Any]) -> list[Any]:
    flattened_list = []
    for element in list_:
        if isinstance(element, list):
            flattened_list.extend(flatten_list(element))
        else:
            flattened_list.append(element)
    return flattened_list


def flatten(list_: NestedList[T]) -> Generator[T, None, None]:
    for element in list_:
        if isinstance(element, list):
            yield from flatten(element)
        else:
            yield element
