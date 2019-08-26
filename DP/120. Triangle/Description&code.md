# Description
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```
The minimum path sum from top to bottom is 11 (i.e., **2** + **3** + **5** + **1** = 11).

**Note:**

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

# Code
```python3
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle == []:
            return 0
        whole = []
        line = []
        for i in range(len(triangle)):
            for j in range(i, len(triangle)):
                line.append(triangle[j][i])
            whole.append(line)
            line = []
        for i in range(len(triangle) - 1):
            for j in range(len(triangle) - 1 - i):
                whole[j][len(triangle) - 2 - i - j] += min(whole[j][len(triangle) - 1 - i - j], whole[j+1][len(triangle) - 2 - i - j])
        return whole[0][0]
```
