from leetcode.graphs.courses import can_finish, find_order


def test_no_prerequisites():
    assert can_finish(3, []) is True
    assert can_finish(1, []) is True


def test_simple_cycle():
    # 0 -> 1 -> 0
    assert can_finish(2, [[0, 1], [1, 0]]) is False


def test_no_cycle():
    # Must take course 1 before course 0
    assert can_finish(2, [[0, 1]]) is True


def test_longer_cycle():
    # 0 -> 1 -> 2 -> 0
    assert can_finish(3, [[0, 1], [1, 2], [2, 0]]) is False


def test_chain_no_cycle():
    # Linear dependency: 0 <- 1 <- 2 <- 3
    assert can_finish(4, [[0, 1], [1, 2], [2, 3]]) is True


def test_multiple_components_no_cycle():
    # Two independent chains
    assert can_finish(4, [[1, 0], [3, 2]]) is True


def test_multiple_prerequisites_no_cycle():
    # Course 2 requires both 0 and 1
    assert can_finish(3, [[2, 0], [2, 1]]) is True


def test_cycle_not_involving_all_nodes():
    # 4 courses, cycle only between courses 0 and 1
    assert can_finish(4, [[1, 0], [0, 1], [3, 2]]) is False


def test_single_course():
    assert can_finish(1, []) is True


def test_disconnected_with_no_cycle():
    # 5 courses, no prerequisites at all
    assert can_finish(5, []) is True


# find_order tests


def is_valid_order(
    order: list[int], num_courses: int, prerequisites: list[list[int]]
) -> bool:
    """Check that every prerequisite b appears before a in order."""
    if len(order) != num_courses:
        return False
    position = {course: i for i, course in enumerate(order)}
    return all(position[b] < position[a] for a, b in prerequisites)


def test_find_order_no_prerequisites():
    order = find_order(3, [])
    assert is_valid_order(order, 3, [])

    order = find_order(1, [])
    assert is_valid_order(order, 1, [])


def test_find_order_simple():
    # Must take 1 before 0
    order = find_order(2, [[0, 1]])
    assert is_valid_order(order, 2, [[0, 1]])


def test_find_order_chain():
    # 3 -> 2 -> 1 -> 0
    prereqs = [[0, 1], [1, 2], [2, 3]]
    order = find_order(4, prereqs)
    assert is_valid_order(order, 4, prereqs)


def test_find_order_multiple_prerequisites():
    # Course 2 requires both 0 and 1
    prereqs = [[2, 0], [2, 1]]
    order = find_order(3, prereqs)
    assert is_valid_order(order, 3, prereqs)


def test_find_order_multiple_components():
    # Two independent pairs
    prereqs = [[1, 0], [3, 2]]
    order = find_order(4, prereqs)
    assert is_valid_order(order, 4, prereqs)


def test_find_order_cycle_returns_empty():
    assert find_order(2, [[0, 1], [1, 0]]) == []
    assert find_order(3, [[0, 1], [1, 2], [2, 0]]) == []


def test_find_order_cycle_not_involving_all_nodes():
    assert find_order(4, [[1, 0], [0, 1], [3, 2]]) == []
