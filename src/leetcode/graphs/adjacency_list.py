def adjacency_list(
    num_nodes: int, edges: list[tuple[int, int]]
) -> dict[int, list[int]]:
    adj: dict[int, list[int]] = {}
    for node in range(num_nodes):
        adj[node] = []

    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    return adj
