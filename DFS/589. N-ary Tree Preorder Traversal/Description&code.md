# Description
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a `3-ary` tree:

```
               1
             / | \
            3  2  4
          /  \
         5    6
```
Return its preorder traversal as: `[1,3,5,6,2,4]`.
**Note:**
Recursive solution is trivial, could you do it iteratively?

# Code
```python3
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ret = []
        stack = []
        stack.append(root)
        while stack != []:
            temp = stack.pop()
            ret.append(temp.val)
            for i in range(len(temp.children) - 1, -1, -1):
                stack.append(temp.children[i])
        return ret
```
