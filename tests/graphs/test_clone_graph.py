from leetcode.graphs.clone_graph import IntGraphNode, clone_graph


def test_simple_graph():
    node = IntGraphNode(1)
    node_2 = IntGraphNode(2)
    node_3 = IntGraphNode(3)

    node.neighbors = [node_2, node_3]
    node_2.neighbors = [node]
    node_3.neighbors = [node]

    adj_list = clone_graph(node)
    assert adj_list == {1: [2, 3], 2: [1], 3: [1]}


def test_other_graph():
    n1 = IntGraphNode(1)
    n2 = IntGraphNode(2)
    n3 = IntGraphNode(3)
    n4 = IntGraphNode(4)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    adj_list = clone_graph(n1)

    assert adj_list == {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
