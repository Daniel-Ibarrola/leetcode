import pytest

from leetcode.recursion.flatten_list import flatten_list, flatten


@pytest.mark.parametrize(
    "items, expected",
    [
        ([1, 2, 3], [1, 2, 3]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([1, [2, 3], 4], [1, 2, 3, 4]),
        ([1, [2, [3, [4, [5]]]]], [1, 2, 3, 4, 5]),
        ([[[[1]]], 2, [[3, 4]], [[[5]]]], [1, 2, 3, 4, 5]),
        ([], []),
        ([[], [[]], [[[]]]], []),
        ([1, [], [2, [], [3]], []], [1, 2, 3]),
        (["a", ["b", ["c"]], "d"], ["a", "b", "c", "d"]),
        ([True, [False, [True]], []], [True, False, True]),
        ([1, [2.5, ["x"]], [[True]], None], [1, 2.5, "x", True, None]),
    ],
)
def test_flatten_list(items, expected):
    assert flatten_list(items) == expected


@pytest.mark.parametrize(
    "items, expected",
    [
        ([1, 2, 3], [1, 2, 3]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([1, [2, 3], 4], [1, 2, 3, 4]),
        ([1, [2, [3, [4, [5]]]]], [1, 2, 3, 4, 5]),
        ([[[[1]]], 2, [[3, 4]], [[[5]]]], [1, 2, 3, 4, 5]),
        ([], []),
        ([[], [[]], [[[]]]], []),
        ([1, [], [2, [], [3]], []], [1, 2, 3]),
        (["a", ["b", ["c"]], "d"], ["a", "b", "c", "d"]),
        ([True, [False, [True]], []], [True, False, True]),
        ([1, [2.5, ["x"]], [[True]], None], [1, 2.5, "x", True, None]),
    ],
)
def test_flatten_list_generator(items, expected):
    assert list(flatten(items)) == expected
