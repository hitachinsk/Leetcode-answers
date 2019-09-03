# Description
Given a binary tree, return the postorder traversal of its nodes' values.

**Example:**
```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
```
**Follow up:** Recursive solution is trivial, could you do it iteratively?

**trivial:easy to implement**

# Code
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # if root == None:
        #     return []
        # ret = []
        # ret += self.postorderTraversal(root.left)
        # ret += self.postorderTraversal(root.right)
        # ret += [root.val]
        # return ret
        if root == None:
            return []
        ret = []
        stack = []
        ret = [root]
        while ret:
            cur = ret.pop()
            stack.append(cur)
            if cur.left != None:
                ret.append(cur.left)
            if cur.right != None:
                ret.append(cur.right)
        while stack:
            ret.append(stack.pop().val)
        return ret
```
