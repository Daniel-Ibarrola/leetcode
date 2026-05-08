# Matrices

**Boundary/Layer Traversal (Spiral)**
Shrink top/bottom/left/right bounds inward after walking each side.
```python
def spiral_order(matrix: list[list[int]]) -> list[int]:
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
```

**In-place Rotation (Transpose + Reverse)**
Rotate 90° clockwise: transpose the matrix, then reverse each row.
```python
def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
```

**Diagonal Grouping**
Elements on the same diagonal share a key: `i - j` (top-left → bottom-right) or `i + j` (anti-diagonal).
```python
# Toeplitz check: all elements on same (i-j) diagonal are equal
def is_toeplitz(matrix: list[list[int]]) -> bool:
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False
    return True

# Collect diagonals for traversal or sorting
from collections import defaultdict
def group_by_diagonal(matrix: list[list[int]]) -> dict:
    diags = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            diags[i - j].append(matrix[i][j])  # use i+j for anti-diagonals
    return diags
```

**Index Linearization (Reshape / Transpose)**
Map 2D `(r, c)` ↔ flat index to reinterpret matrix shape.
```python
def reshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat
    flat = [mat[i][j] for i in range(m) for j in range(n)]
    return [[flat[i * c + j] for j in range(c)] for i in range(r)]
```

**Fixed-size Submatrix Scan**
Slide a `k×k` window over all valid positions `(i, j)` where `0 <= i,j <= n-k`.
```python
def largest_local(grid: list[list[int]], k: int) -> list[list[int]]:
    n = len(grid)
    return [
        [max(grid[r][c] for r in range(i, i + k) for c in range(j, j + k))
         for j in range(n - k + 1)]
        for i in range(n - k + 1)
    ]
```

**2D DP on Submatrices**
`dp[i][j]` depends on the three neighbors above/left. Classic for counting/sizing squares or rectangles.
```python
# dp[i][j] = side length of largest square of 1s with bottom-right corner at (i, j)
def count_squares(matrix: list[list[int]]) -> int:
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] and i > 0 and j > 0:
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
            count += matrix[i][j]
    return count
```
