def is_valid_tree(num_nodes: int, edges: list[list[int]]) -> bool:
    adjacency_list: dict[int, list[int]] = {node: [] for node in range(num_nodes)}
    for edge in edges:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])

    if not adjacency_list:
        return True

    visited: list[bool] = [False] * num_nodes

    def has_cycle(node: int, origin: int) -> bool:
        if visited[node]:
            return True

        visited[node] = True
        for neighbor in adjacency_list[node]:
            if neighbor == origin:
                continue
            if has_cycle(neighbor, node):
                return True

        return False

    if has_cycle(0, -1):
        return False

    return all(visited)
