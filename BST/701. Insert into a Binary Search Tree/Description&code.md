# Description
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example:
```
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
```
You can return this binary search tree:
```
         4
       /   \
      2     7
     / \   /
    1   3 5
```
This tree is also valid:
```
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        p = root
        while True:
            if val < p.val:
                if p.left is not None:
                    p = p.left
                else:
                    flag = True # left
                    break
            elif val > p.val:
                if p.right is not None:
                    p = p.right
                else:
                    flag = False # right
                    break
            else:
                return root
        if flag == True:
            p.left = TreeNode(val)
        else:
            p.right = TreeNode(val)
        return root
```
