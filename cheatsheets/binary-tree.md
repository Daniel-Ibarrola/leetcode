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
        # number of nodes at the current level
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            curr = queue.popleft()
            current_level.append(curr.val)            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        # we have finished processing all nodes at the current level
        result.append(current_level)
        
    return result
```
