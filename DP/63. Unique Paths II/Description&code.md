# Description
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as `1` and `0` respectively in the grid.

**Note:** m and n will be at most 100.

**Example 1:**
```
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

# Code
```python3
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid == []:
            return 0
        path_store = [0] * len(obstacleGrid[0])
        for i in range(len(path_store) - 1, -1, -1):
            if obstacleGrid[-1][i] == 1:
                break
            path_store[i] = 1
        for i in range(len(obstacleGrid) - 2, -1, -1):
            for j in range(len(path_store)-1, -1, -1):
                if j == len(path_store) - 1:
                    if obstacleGrid[i][j] == 1:
                        path_store[j] = 0
                else:
                    if obstacleGrid[i][j] == 0:
                        path_store[j] = path_store[j] + path_store[j + 1]
                    else:
                        path_store[j] = 0
        return path_store[0]
```
