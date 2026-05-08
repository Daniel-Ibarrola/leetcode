# Graph

**DFS**
```python
def dfs(adj_list):
    if not adj_list:
        return
    visited = set()

    def dfs_helper(node):
        if node in visited:
            return

        visited.add(node)
        for neighbor in adj_list[node]:
            dfs_helper(neighbor)
        return

    # Handle disconnected components
    for node in adj_list:
        if node not in visited:
            dfs_helper(node)
```

**BFS**
```python
def bfs(graph, start):
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
```
