# Desctiption
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree `[1,2,2,3,4,4,3]` is symmetric:
```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```
But the following `[1,2,2,null,3,null,3]` is not:
```
    1
   / \
  2   2
   \   \
   3    3
```
Note:
Bonus points if you could solve it both recursively and iteratively. 

#code
* Recursively
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if (not root) or (not root.left and not root.right):
            return True
        if root.left and root.right and root.left.val == root.right.val:
            if self.elemsEqual(root.left, root.right):
                return True
        return False
           
           
    def elemsEqual(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val == node2.val:
            return self.elemsEqual(node1.left, node2.right) and self.elemsEqual(node1.right, node2.left)
        else:
            return False
```
* Iteratively
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if (not root) or (not root.left and not root.right):
            return True
        if root.left and root.right and root.left.val == root.right.val:
            queue = [root]
            elemnums = 1
            while queue != []:
                elemnum_store = 0
                for i in range(elemnums):
                    k = queue.pop(0)
                    if isinstance(k, int):
                        continue
                    if k.left:
                        queue.append(k.left)
                        elemnum_store += 1
                    else:
                        queue.append(0)
                        elemnum_store += 1
                    if k.right:
                        queue.append(k.right)
                        elemnum_store += 1
                    else:
                        queue.append(0)
                        elemnum_store += 1
                queue_values = self.qvs(queue)
                queue_store = queue_values[:]
                queue_values.reverse()
                if queue_values != queue_store:
                    return False
                elemnums = elemnum_store
            return True
        else:
            return False
        
    
    def qvs(self, queue):
        res = []
        for each in queue:
            try:
                res.append(each.val)
            except:
                res.append(0)
        return res
```
        
