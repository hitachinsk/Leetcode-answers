这道题还是不容易做的，相比于之前的版本，这道题已经不满足于找到搜索二叉树的个数，而是要生成全部的搜索二叉树。

与之前题目的思路相类似，对于任何一个元素个数为n的搜索二叉树的生成都是由元素个数为n-1， n-2 ... 一直到1的搜索二叉树生成的，所以对于这道题也采用相似的
套路进行。

- 首先，对于元素个数为n的搜索二叉树生成，需要便利元素的所有节点并分别把这些节点当作根节点，这样其余节点就会在这个节点两侧被分割为左节点组和右节点
组。

- 然后，对于左节点组和右节点组分别进行搜索二叉树的生成， 每一个节点组生成的搜索二叉树可能不止一个
- 最后，将左节点组和右节点组生成的搜索二叉树分别拼接到根节点的左右两侧，形成一个个搜索二叉树

这就是本题基本的思路框架，但是多元素的搜索二叉树一定需要用到少量元素的搜索二叉树结构，因此如果要求解一个元素个数为n的搜索二叉树需要把元素为1，2，
... n-1的搜索二叉树全部生成一遍，然后把这些搜索二叉树的结构储存起来以便元素组生成搜索二叉树的时候使用。在本题我选择了字典。

但是对于不同元素的搜索二叉树而言，多元素从少元素的搜索二叉树只能借鉴搜索二叉树的结构，而其中含有的元素需要重新赋予。例如说，如果需要生成19，20两个
元素组成的二叉搜索树，其基本结构与1，2这两个元素生成的二叉搜索树是一致的，唯独每个元素不同，所以为了解决这个问题，我实现了`traverse`以及`copyTree`两个
函数。`traverse`采用了层序遍历来得到树当中的每个元素，便于修改元素内容值，而`copyTree`则是将当前树进行拷贝，目的是变化树元素的过程当中不影响原有
树的元素值。

而`combine`函数则是将生成的左和右子树组拼接在根元素两侧，在拼接的时候一定要注意，拼接之后需要将得到的树拷贝才能存到结果数组当中，并且
每一次循环之后都要将根节点的左子树和右子树置为空，否则根元素就会改变
从而不能得到正确的结果
