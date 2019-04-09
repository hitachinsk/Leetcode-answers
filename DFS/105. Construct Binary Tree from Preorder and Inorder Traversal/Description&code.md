# Description
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == [] or inorder == []:
            return None
        leftchildren = []
        rightchildren = []
        root = preorder[0]
        flag = False
        for i in range(len(inorder)):
            if inorder[i] != root and flag == False:
                leftchildren.append(inorder[i])
            elif inorder[i] == root:
                flag = True
            elif inorder[i] != root and flag == True:
                rightchildren.append(inorder[i])
            else:
                raise ValueError('Unknown mistake')
        leftchildren_preorder = preorder[1 : 1+len(leftchildren)]
        rightchildren_preorder = preorder[1+len(leftchildren) : len(preorder)]
        
        left = self.buildTree(leftchildren_preorder, leftchildren)
        right = self.buildTree(rightchildren_preorder, rightchildren)
        
        rootNode = TreeNode(root)
        rootNode.left = left
        rootNode.right = right
        return rootNode
```
                
        
        
