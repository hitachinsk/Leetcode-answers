这道题同样采用递归的做法实现，其实盯住一个关系式就可以
```
树的左叶子之和=左子树的左叶子之和+右子树的左叶子之和
```
但是为了记录左子树和右子树需要引入额外的一个参数告诉函数当前节点是其父节点的左子树还是右子树，如果是左子树并且是叶子节点那么这个
节点的值就将会被记录，否则不会被记录（返回0），如果当前处理的节点为空也直接返回0即可