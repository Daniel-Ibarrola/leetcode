from collections import defaultdict


def longest_path(n: int, edges: list[list[int]]) -> int:
    """
    Given a directed acyclic graph (DAG) with n nodes labeled 0 to n - 1,
    and a list of directed edges where edges[i] = [u, v] means there is a
    directed edge from u to v, return the length of the longest path in the
    graph (measured in number of edges).

    Example 1:
        Input: n = 6, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [3, 5]]
        Output: 3
        Explanation: The longest path is 0 → 1 → 3 → 4 (or 0 → 2 → 3 → 5), length 3.

    Example 2:
        Input: n = 3, edges = [[0, 1], [1, 2]]
        Output: 2
        Explanation: The longest path is 0 → 1 → 2, length 2.

    Example 3:
        Input: n = 1, edges = []
        Output: 0
        Explanation: A single node has no edges, so the longest path has length 0.

    Constraints:
        - 1 <= n <= 1000
        - 0 <= edges.length <= n * (n - 1) / 2
        - edges[i].length == 2
        - 0 <= edges[i][0], edges[i][1] < n
        - The input graph is guaranteed to be a DAG (no cycles).
    """
    graph = defaultdict(list)
    for from_node, to_node in edges:
        graph[from_node].append(to_node)

    longest_found: dict[int, int] = {}

    def dfs(node: int) -> int:
        if node in longest_found:
            return longest_found[node]

        max_from_neighbors = 0
        for neighbor in graph[node]:
            max_from_neighbors = max(dfs(neighbor) + 1, max_from_neighbors)

        longest_found[node] = max_from_neighbors
        return max_from_neighbors

    max_len = 0
    for node in range(n):
        max_len = max(dfs(node), max_len)

    return max_len
