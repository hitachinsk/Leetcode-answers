本题其实是栈回溯的一个代表, 本题的主要要求就是在找到栈最小元素的时候操作必须是`O(1)`的,因此就需要在每一次将元素`push`和`pop`的时候记录当前栈当中元素的最小值

那么,如何记录才能够在记录栈最小值的同时又能够在每一次元素出栈之后能够回溯到之前栈的最小元素呢?

首先,记录最小元素的数据结构也必须使用一个列表`self.min`,因为要涉及到回溯操作.其次,在每次有元素`push`进入这个栈的时候需要与`self.min`的最末一位进行比较,如果小于`self.min`的
最末一位元素,表示当前栈有新的最小值进入,就需要更新`self.min`,将该元素`append`到这个列表当中,如果等于最末一位元素也要将其`append`到`self.min`当中(说明在后面),如果大于则什么都不干.

在`pop`操作的时候,如果`pop`出来的元素与`self.min`最末一位元素相等,则对`self.min`也进行`pop`处理,反之什么都不干.

考虑如下情况:
```
10->8->4->2->2->2
```
如果等于的情况下不把该元素`append`到最小值列表的话,那么`self.min`增长顺序如下所示.
```
10->8->4->2
```
此时如果`pop`末尾元素`2`,那么就要把`self.min`当中末尾元素也删掉,那么`self.min`就会变成
```
10->8->4
```
但是此时栈当中元素为
```
10->8->4->2->2
```
最小元素还是2,与`self.min`当中的记录不符,所以当`push`进去的元素与`self.min`最末一位相等时也要压入`self.min`当中,这样在删除的时候才能保证两者之间的同步.

