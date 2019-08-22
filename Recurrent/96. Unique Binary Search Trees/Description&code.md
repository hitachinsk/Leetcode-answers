# Description
Given n, how many structurally unique **BST's** (binary search trees) that store values 1 ... n?

**Example:**
```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

# Code
```python3
class Solution:
    def __init__(self):
        self.cache = {}
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        if n in self.cache:
            return self.cache[n]
        ret = 0
        for i in range(n // 2):
            ret += self.numTrees(i) * self.numTrees(n-1-i)
        ret = ret * 2
        if n % 2 == 1:
            ret += self.numTrees((n-1) // 2) ** 2
        self.cache[n] = ret
        return ret
```
