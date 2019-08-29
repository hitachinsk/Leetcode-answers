本题倒是很好读懂，但是我并没有什么好的头绪，采用暴力方法求解，没想到还过了。

其实本题的难点在于如何判断相邻的节点总和是否为`0`，因为题目当中并没有对相邻节点的个数加以限制，可以是`1`个相邻节点，也可以是一堆相邻节点。我采用了双指针
遍历链表的暴力搜索方式解答此题。

首先，对与任何一个链表，找到其头元素，用一个指针p指向它，然后判断这个元素是否为`0`，为`0`则删去，如果当前元素是`head`则需要将`head`后移。如果不是`0`，则需要
在`p.next`开辟一个额外的指针`q`，将`p.val`和`q.val`加起来看是否为`0`，为`0`则删去这些元素，不为`0`则将`q`向后移动，然后将`p`和`q`之间的元素加和判断是否为`0`直到`q`出界然后
将`p`向后移动直到`p`也出界。最终返回条件就是再一次遍历循环当中找不到加和为`0`的相邻元素组。

本题需要对边界条件做出一些讨论，如果输入链表为空的话输出链表自然为空，如果输入链表只有一个元素那么就要判断这个节点的元素是否为`0`，如果为`0`删除元素返回`None`，
反之不删除直接返回`head`