# Description
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a `3-ary` tree:
```
            1
          / | \
         3  2  4
        / \
       5   6
```
Return its postorder traversal as: `[5,6,3,2,4,1]`.

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
    def postorder(self, root: 'Node') -> List[int]:
        # if root == None:
        #     return None
        # ret = []
        # for elem in root.children:
        #     ret += self.postorder(elem)
        # ret += [root.val]
        # return ret
        
        if root == None:
            return None
        ret = []
        stack = []
        ret += [root]
        while ret:
            cur = ret.pop()
            stack.append(cur)
            ret.extend(cur.children)
        while stack:
            cur = stack.pop()
            ret.append(cur.val)
        return ret
```
