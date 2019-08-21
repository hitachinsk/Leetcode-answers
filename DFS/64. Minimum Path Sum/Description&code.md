# Description
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

**Example:**
```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```
# Code
```python3
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid == []:
            return 0
        path_store = [0] * len(grid[0])
        for i in range(len(grid) - 1, -1, -1):
            if i == len(grid) - 1:
                for j in range(len(grid[0]) - 1, -1, -1):
                    if j == len(grid[0]) - 1:
                        path_store[j] = grid[i][j]
                    else:
                        path_store[j] = grid[i][j] + path_store[j+1]
            else:
                for j in range(len(grid[0]) - 1, -1, -1):
                    if j == len(grid[0] ) - 1:
                        path_store[j] += grid[i][j]
                    else:
                        path_store[j] = min(path_store[j + 1], path_store[j]) + grid[i][j]
        return path_store[0]
```
