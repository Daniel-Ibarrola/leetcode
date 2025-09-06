from leetcode.graphs.adjacency_list import adjacency_list


def test_adjacency_list():
    num_nodes = 4
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
    expected = {0: [1, 3, 2], 1: [0, 2], 2: [1, 3, 0], 3: [2, 0]}
    assert adjacency_list(num_nodes, edges) == expected
