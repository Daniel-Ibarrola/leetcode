# Binary Tree

**DFS**
```python
def dfs(node):
    # base case
    if node is None:
        return some value

    ...

    left = dfs(node.left)
    right = dfs(node.right)
    return value based on left and right
```

**BFS**
```python
def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        curr_node = queue.popleft()
        result.append(curr_node.val)

        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)

    return result
```
