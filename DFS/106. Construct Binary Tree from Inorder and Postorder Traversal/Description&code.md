# Description
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
```
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```
Return the following binary tree:
```
    3
   / \
  9  20
    /  \
   15   7
```

# Code
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder == []:
            return None
        root = postorder[-1]
        leftchildren = []
        rightchildren = []
        leftchildren_post = []
        rightchildren_post = []
        for i in range(len(inorder)):
            if inorder[i] == root:
                leftchildren = inorder[:i]
                rightchildren = inorder[i+1:]
                leftchildren_post = postorder[:len(leftchildren)]
                rightchildren_post = postorder[len(leftchildren):len(leftchildren) + len(rightchildren)]
                break
        rootNode = TreeNode(root)
        rootNode.left = self.buildTree(leftchildren, leftchildren_post)
        rootNode.right = self.buildTree(rightchildren, rightchildren_post)
        return rootNode
```
