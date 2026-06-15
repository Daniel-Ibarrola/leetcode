from leetcode.backtracking.subsets import subsets


def normalize(result: list[list[int]]) -> set[tuple[int, ...]]:
    return {tuple(sorted(s)) for s in result}


def test_single_element():
    result = subsets([1])
    assert normalize(result) == {(), (1,)}


def test_two_elements():
    result = subsets([1, 2])
    assert normalize(result) == {(), (1,), (2,), (1, 2)}


def test_three_elements():
    result = subsets([1, 2, 3])
    assert normalize(result) == {
        (),
        (1,),
        (2,),
        (3,),
        (1, 2),
        (1, 3),
        (2, 3),
        (1, 2, 3),
    }


def test_empty_input():
    result = subsets([])
    assert normalize(result) == {()}


def test_subset_count():
    # 2^n subsets for n unique elements
    for n in range(1, 5):
        nums = list(range(n))
        assert len(subsets(nums)) == 2**n


def test_no_duplicate_subsets():
    result = subsets([1, 2, 3])
    normalized = [tuple(sorted(s)) for s in result]
    assert len(normalized) == len(set(normalized))


def test_negative_numbers():
    result = subsets([-1, 0, 1])
    assert normalize(result) == {
        (),
        (-1,),
        (0,),
        (1,),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (-1, 0, 1),
    }


def test_returns_list_of_lists():
    result = subsets([1, 2])
    assert isinstance(result, list)
    assert all(isinstance(s, list) for s in result)
