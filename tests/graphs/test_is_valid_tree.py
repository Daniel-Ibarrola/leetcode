from leetcode.graphs.is_valid_tree import is_valid_tree


def test_disconnected_graph():
    # A graph with 4 nodes and 2 edges forming two separate components
    assert is_valid_tree(4, [[0, 1], [2, 3]]) is False

    # A graph with 5 nodes where one node is disconnected
    assert is_valid_tree(5, [[0, 1], [1, 2], [2, 3]]) is False


def test_cyclic_graph():
    # A graph with 3 nodes forming a cycle
    assert is_valid_tree(3, [[0, 1], [1, 2], [2, 0]]) is False

    # A graph with 4 nodes with a cycle
    assert is_valid_tree(4, [[0, 1], [1, 2], [2, 3], [3, 1]]) is False


def test_valid_tree():
    # A simple tree with 5 nodes and 4 edges
    assert is_valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])

    # A line graph
    assert is_valid_tree(4, [[0, 1], [1, 2], [2, 3]])

    # A single node graph
    assert is_valid_tree(1, [])

    # A two-node graph
    assert is_valid_tree(2, [[0, 1]])

    # An empty graph
    assert is_valid_tree(0, [])
