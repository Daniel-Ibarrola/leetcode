import enum


class Color(enum.Enum):
    NO_COLOR = 1
    RED = 2
    GREEN = 3

def is_bipartite(graph: list[list[int]]) -> bool:
    """
    There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1.
    You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to.

    A graph is bipartite if the nodes can be partitioned into two independent sets A and B such
    that every edge in the graph connects a node in set A to a node in set B.

    Return true if and only if the graph is bipartite.

    Example 1:
        Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
        Output: false
        Explanation: There is no way to partition the nodes into two independent sets such that
        every edge connects a node in one set to a node in the other.

    Example 2:
        Input: graph = [[1,3],[0,2],[1,3],[0,2]]
        Output: true
        Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

    Constraints:
        - graph.length == n
        - 1 <= n <= 100
        - 0 <= graph[u].length < n
        - 0 <= graph[u][i] <= n - 1
        - graph[u] does not contain u (no self-loops)
        - All values of graph[u] are unique
        - If graph[u] contains v, then graph[v] contains u (undirected)
    """
    colors: dict[int, Color] = {n: Color.NO_COLOR for n in range(len(graph))}

    def has_odd_cycle(node: int, prev_color: Color, current_color: Color) -> bool:
        if colors[node] != Color.NO_COLOR:
            return colors[node] == prev_color

        colors[node] = current_color
        next_color = Color.RED if current_color == Color.GREEN else Color.GREEN
        for neighbor in graph[node]:
            if has_odd_cycle(neighbor, current_color, next_color):
                return True

        return False

    for n in range(len(graph)):
        if colors[n] == Color.NO_COLOR and has_odd_cycle(n, Color.NO_COLOR, Color.RED):
            return False

    return True
