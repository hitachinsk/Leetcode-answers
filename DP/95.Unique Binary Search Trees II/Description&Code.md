# Description
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

**Example:**
```
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
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
    def generateTrees(self, n: int) -> List[TreeNode]:
        ret = {}
        ret[0] = []
        part_ret = []
        for i in range(n):
            ret[i+1] = part_ret
            if i == 0:
                ret[i+1].append(TreeNode(1))
            else:
                for root in range(1, i+2):
                    root_node = TreeNode(root)
                    left_nodes = [m for m in range(1, root)]
                    right_nodes = [m for m in range(root+1, i+2)]
                    root_node_left_group = self.createTree(ret[len(left_nodes)], left_nodes)
                    root_node_right_group = self.createTree(ret[len(right_nodes)], right_nodes)
                    kkp = self.combine(root_node, root_node_left_group, root_node_right_group)
                    part_ret.extend(kkp)
                ret[i+1] = part_ret
            part_ret = []
        return ret[n]
            
    def createTree(self, forest, nodes):
        if forest == [] or nodes == []:
            return []
        max_elem = max(nodes)
        min_elem = min(nodes)
        ret = []
        for tree in forest:
            ret.append(self.traverse(max_elem, min_elem, tree))
        return ret
    
    def combine(self, root, left_group, right_group):
        ret = []
        if left_group == [] and right_group == []:
            return root
        if left_group == [] and right_group != []:
            root.left = None
            for each in right_group:
                root.right = each
                ret.append(self.copyTree(root))
                root.right = None
        elif left_group != [] and right_group == []:
            root.right = None
            for each in left_group:
                root.left = each
                ret.append(self.copyTree(root))
                root.left = None
        else:
            for each in left_group:
                root.left = each
                for ones in right_group:
                    root.right = ones
                    ret.append(self.copyTree(root))
                    root.right = None
                root.left = None
        return ret
    
    def traverse(self, max_elem, min_elem, tree):
        newTree = self.copyTree(tree)
        queue = []
        queue.append(newTree)
        while queue != []:
            temp = queue.pop(0)
            temp.val += (min_elem - 1)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
        return newTree
    
    def copyTree(self, tree):
        if tree is None:
            return None
        ret = TreeNode(tree.val)
        ret.left = self.copyTree(tree.left)
        ret.right = self.copyTree(tree.right)
        return ret
```
