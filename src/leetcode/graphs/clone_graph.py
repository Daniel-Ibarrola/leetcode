from typing import Optional


class IntGraphNode:
    def __init__(
        self, value: int = 0, neighbors: Optional[list["IntGraphNode"]] = None
    ):
        self.value: int = value
        self.neighbors: list["IntGraphNode"] = (
            neighbors if neighbors is not None else []
        )


def clone_graph(node: IntGraphNode) -> dict[int, list[int]]:
    adj_list: dict[int, list[int]] = {}

    def dfs(current_node: IntGraphNode) -> None:
        if current_node.value in adj_list:
            return

        adj_list[current_node.value] = [n.value for n in current_node.neighbors]

        for neighbor in current_node.neighbors:
            dfs(neighbor)

    dfs(node)
    return adj_list
