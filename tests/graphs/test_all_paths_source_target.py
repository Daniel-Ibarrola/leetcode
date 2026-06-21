from leetcode.graphs.all_paths_source_target import all_paths_source_target


def test_two_paths():
    # 0 -> 1 -> 3 and 0 -> 2 -> 3
    graph = [[1, 2], [3], [3], []]
    result = sorted(map(tuple, all_paths_source_target(graph)))
    expected = sorted([(0, 1, 3), (0, 2, 3)])
    assert result == expected


def test_multiple_paths():
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    result = sorted(map(tuple, all_paths_source_target(graph)))
    expected = sorted([(0, 4), (0, 3, 4), (0, 1, 3, 4), (0, 1, 2, 3, 4), (0, 1, 4)])
    assert result == expected


def test_direct_edge_only():
    # Only one path: 0 -> 1
    graph = [[1], []]
    result = all_paths_source_target(graph)
    assert result == [[0, 1]]


def test_linear_chain():
    # Only one path: 0 -> 1 -> 2 -> 3
    graph = [[1], [2], [3], []]
    result = all_paths_source_target(graph)
    assert result == [[0, 1, 2, 3]]


def test_all_nodes_connect_to_target():
    # 0 -> 1, 0 -> 2, 0 -> 3 (target); also 1 -> 3, 2 -> 3
    graph = [[1, 2, 3], [3], [3], []]
    result = sorted(map(tuple, all_paths_source_target(graph)))
    expected = sorted([(0, 3), (0, 1, 3), (0, 2, 3)])
    assert result == expected


def test_wide_branching():
    # Node 0 connects directly to all others, each also connects to the last node
    graph = [[1, 2, 3], [3], [3], []]
    result = sorted(map(tuple, all_paths_source_target(graph)))
    assert len(result) == 3
