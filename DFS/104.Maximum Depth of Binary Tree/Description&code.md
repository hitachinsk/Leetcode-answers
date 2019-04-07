# Description
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],
```
    3
   / \
  9  20
    /  \
   15   7
```
return its depth = 3.

# Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res, height = 0, 1
        if not root:
            return res
        paths = [root]
        idx = 0
        while idx >= 0:
            while paths[idx].left or paths[idx].right:
                if paths[idx].left:
                    paths.append(paths[idx].left)
                    paths[idx].left = None
                    idx += 1
                    height += 1
                else:
                    paths.append(paths[idx].right)
                    paths[idx].right = None
                    idx += 1
                    height += 1
            if height > res:
                res = height
            paths.pop()
            height -= 1
            idx -= 1
        return res
```
