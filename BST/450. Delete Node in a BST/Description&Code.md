# Description
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
- Search for a node to remove.
- If the node is found, delete the node.

**Note**: Time complexity should be O(height of tree).

**Example:**
```
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
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
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return None
        if root.val == key:
            if root.left == None and root.right == None:
                return None
            if root.left != None and root.right == None:
                root = root.left
                return root
            if root.left == None and root.right != None:
                root = root.right
                return root
            left_pointer = root.left
            right_connector = self.findRightMin(root.right)
            root = root.right
            right_connector.left = left_pointer
            return root
        p = root
        parent = None
        direction = None
        while p.left != None or p.right != None:
            if key < p.val:
                parent = p
                direction = 0 # 0 is left, 1 is right
                p = p.left
            elif key > p.val:
                parent = p
                direction = 1
                p = p.right
            else:
                if p.left != None and p.right == None:
                    if direction == 0:
                        parent.left = p.left
                    elif direction == 1:
                        parent.right = p.left
                elif p.left == None and p.right != None:
                    if direction == 0:
                        parent.left = p.right
                    elif direction == 1:
                        parent.right = p.right
                else:
                    left_pointer = p.left
                    right_connector = self.findRightMin(p.right)
                    if direction == 0:
                        parent.left = p.right
                    elif direction == 1:
                        parent.right = p.right
                    right_connector.left = left_pointer
                return root
        if p == None or p.val != key:
            return root
        if direction == 0:
            parent.left = None
        elif direction == 1:
            parent.right = None
        return root
        
    def findRightMin(self, root):
        p = root
        while p.left != None:
            p = p.left
        return p
```
