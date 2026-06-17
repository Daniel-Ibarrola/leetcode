from leetcode.graphs.longest_path_dag import longest_path


def test_single_node():
    assert longest_path(1, []) == 0


def test_two_nodes():
    assert longest_path(2, [[0, 1]]) == 1


def test_linear_chain():
    # 0 → 1 → 2 → 3
    assert longest_path(4, [[0, 1], [1, 2], [2, 3]]) == 3


def test_branching_paths():
    # 0 → 1 → 3
    # 0 → 2 → 3 → 4 → 5  (longest)
    assert longest_path(6, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [3, 5]]) == 3


def test_diamond_shape():
    # 0 → 1 → 3
    # 0 → 2 → 3
    # Both paths have length 2
    assert longest_path(4, [[0, 1], [0, 2], [1, 3], [2, 3]]) == 2


def test_disconnected_graph():
    # Two separate chains: 0 → 1 → 2  and  3 → 4
    # Longest is 0 → 1 → 2, length 2
    assert longest_path(5, [[0, 1], [1, 2], [3, 4]]) == 2


def test_no_edges():
    # 4 isolated nodes
    assert longest_path(4, []) == 0


def test_multiple_sources():
    # 0 → 2
    # 1 → 2 → 3  (longest, length 2)
    assert longest_path(4, [[0, 2], [1, 2], [2, 3]]) == 2


def test_wide_tree():
    # 0 → 1, 0 → 2, 0 → 3, 0 → 4 — all leaf children, longest path is 1
    assert longest_path(5, [[0, 1], [0, 2], [0, 3], [0, 4]]) == 1


def test_long_then_wide():
    # 0 → 1 → 2 → 3, plus 3 → 4 and 3 → 5 — longest is 0 → 1 → 2 → 3 → 4, length 4
    assert longest_path(6, [[0, 1], [1, 2], [2, 3], [3, 4], [3, 5]]) == 4
