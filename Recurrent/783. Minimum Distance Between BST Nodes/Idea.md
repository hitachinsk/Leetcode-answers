这道题主要是用到了二叉搜索树(BST)的性质.对于任何BST而言,左子树节点一定小于根节点,而右子树节点一定大于根节点.那么对BST进行中序遍历的话就必然得到
一个升序序列,而在遍历的时候如果能够对刚遍历的节点和当前节点做差,那么求出最小的那个差值即为本题所求.

中序遍历的递归算法如下:
- 在`root.left`调用原函数
- 对中间的节点进行符合题目的操作
- 在`root.right`调用原函数

而对于本题而言符合题目的操作就是将之前遍历得到节点与当前节点的差值与最小结果进行比较选出更小的那个.而在这里,需要对`python3`的类进行初始化调用从而初始化
`self.pre`和`self.minRet`两个节点从而在函数内部进行修改即可.

而对于中序遍历非递归算法,有人也写了一个函数如下所示.
```cpp
stack<TreeNode*> myStack;
        //非递归中序遍历法
        while (!myStack.empty() || root != NULL){
            while (root != NULL){
                myStack.push(root);//保存现场
                root = root->left;//转移现场到左子树
            }
            root = myStack.top();//回复现场
            myStack.pop();
            minRes = min(minRes, root->val - preVal);//访问现场根节点
            preVal = root->val;//更新中序遍历前一个元素的值
            root = root->right;//转移到右子树
        }
```
那么对于非递归算法而言,操作如下所示.
- 当当前节点不为空或者栈不为空的时候,重复如下操作
- 如果当前节点`root`左子树一直存在,那么不断将当前节点左子树节点压入栈当中
- 将当前节点指向栈顶并将当前节点弹出对此节点进行符合题目的操作
- 当前节点转移到当前节点右子节点

所以修改之后的python3代码如下所示
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.minRet = 1e6
        self.pre = 1e6
        
    def minDiffInBST(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.minRet
    
    def dfs(self, root):
        stack = []
        while stack != [] or root != None:
            while root:
                stack.append(root)
                root = root.left
            root = stack[-1]
            stack.pop()
            self.minRet = min(self.minRet, abs(self.pre - root.val))
            self.pre = root.val
            root = root.right
```
