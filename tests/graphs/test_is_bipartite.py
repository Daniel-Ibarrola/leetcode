from leetcode.graphs.is_bipartite import is_bipartite


def test_not_bipartite_odd_cycle():
    # Triangle: 0-1-2-0, odd cycle cannot be 2-colored
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    assert is_bipartite(graph) is False


def test_bipartite_even_cycle():
    # Even cycle 0-1-2-3-0 can be split into {0,2} and {1,3}
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    assert is_bipartite(graph) is True


def test_single_node():
    assert is_bipartite([[]]) is True


def test_two_nodes_connected():
    graph = [[1], [0]]
    assert is_bipartite(graph) is True


def test_disconnected_bipartite():
    # Two separate edges: 0-1 and 2-3, both bipartite
    graph = [[1], [0], [3], [2]]
    assert is_bipartite(graph) is True


def test_disconnected_with_odd_cycle():
    # One component is a triangle (not bipartite), other is a single edge
    graph = [[1, 2], [0, 2], [0, 1], [4], [3]]
    assert is_bipartite(graph) is False


def test_no_edges():
    # Isolated nodes with no edges are trivially bipartite
    graph = [[], [], [], []]
    assert is_bipartite(graph) is True


def test_complete_bipartite():
    # K2,2: nodes {0,1} each connect to {2,3}
    graph = [[2, 3], [2, 3], [0, 1], [0, 1]]
    assert is_bipartite(graph) is True
