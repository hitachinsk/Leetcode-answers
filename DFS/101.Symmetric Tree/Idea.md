对于这道题我给出了两种解决方案，分别是递归(Recursively)以及迭代(Iteratively)
* 递归(Recursively)

递归的方案需要借助额外的递归判断函数来实现。其实判断一个树是不是对称树的方法就是从根节点出发，首先判断根节点是否为空，如果为空就返回`True`，否则就判断
根节点的两个子树是否存在，如果都不存在返回`True`，只存在一个返回`False`，如果都存在的话就需要判断第一个节点的左子树和第二个节点的右子树根节点
的值是否相同，同时判断第一个节点的右子树根节点的值和第二个节点的左子树的根节点的值是否相同，如果相同就再进行子树的子树的递归，不同的话就直接
返回`False`。递归的退出条件是两个根节点是否存在，都不存在返回`True`，存在一个返回`False`，存在两个就返回向下递归的值。

* 迭代(Itratively)

迭代的方案很简单，层序遍历，每一次遍历就把之前层的元素全部取出，遍历取出的元素并将下一层的元素插入列表当中，判断的时候将列表进行反转，如果反转后
的列表与反转之前的元素值相同的话就继续判断，否则就返回`False`，当列表最后为空的时候就返回`True`。这里有一个地方需要特别注意，当某个节点的左子树或
右子树不存在的时候就需要额外插入一个占位符（这里我设置为0），因为二叉树是有方向的。
