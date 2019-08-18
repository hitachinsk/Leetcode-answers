# Description
给你一个二叉树的根节点 `root`。设根节点位于二叉树的第 `1` 层，而根节点的子节点位于第 `2` 层，依此类推。

请你找出层内元素之和 **最大** 的那几层（可能只有一层）的层号，并返回其中 **最小** 的那个。

**Example:**
```
          1
        /   \
       7     0
      / \
     7   -8
```
```
输入：[1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。
```
**提示:**
1.树中的节点数介于 `1` 和 `10^4` 之间

2.`-10^5 <= node.val <= 10^5`
# Code
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root is None:
            return 1
        stack = []
        max_layer = 1
        current_layer = 1
        max_elems = root.val
        elems = 0
        stack.append(root)
        stack.append('s')
        flag = False
        while stack != []:
            temp = stack.pop(0)
            while temp != 's':
                flag = False
                elems += temp.val
                if temp.left is not None:
                    stack.append(temp.left)
                if temp.right is not None:
                    stack.append(temp.right)
                temp = stack.pop(0)
            print(elems, current_layer, max_elems)
            if flag == True:
                return max_layer
            if elems > max_elems:
                max_layer = current_layer
                max_elems = elems
            current_layer += 1
            stack.append('s')
            flag = True
            elems = 0
 ```
