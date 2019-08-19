# Description
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

**Note:** m and n will be at most 100.

**Example1:**
```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
```
**Example2:**
```
Input: m = 7, n = 3
Output: 28
```

# Code
```python3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_store = [1] * n
        for i in range(m - 1):
            for j in range(n - 1, -1, -1):
                if j == n - 1:
                    path_store[j] = 1
                else:
                    path_store[j] += path_store[j + 1]
        return path_store[0]
```
