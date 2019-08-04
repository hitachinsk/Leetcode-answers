# Description
Find the sum of all left leaves in a given binary tree.
## Example
```
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
```
# Code
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.calcSumOfLeftLeaves(root, "right")
        
    def calcSumOfLeftLeaves(self, node, lr):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            if lr == "left":
                return node.val
            else:
                return 0
        return self.calcSumOfLeftLeaves(node.left, "left") + self.calcSumOfLeftLeaves(node.right, "right")
```
