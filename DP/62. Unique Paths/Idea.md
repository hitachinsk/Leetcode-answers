其实从道理来讲,动态规划(DP)主要还是要找到递归关系,如果找到步进递归关系再画步进表格就很容易求解.

对于本题来讲有如下的关系式:`Path(a,b) = Path(a+1, b) + Path(a, b+1)`

这是一个General的关系式,没有考虑边界情况,对于右边界和下边界而言,路径种类数目都是1,因为机器人只允许往下面或者右边走.

而对于其余点来讲,只需要按照关系式去运算然后画表分别填充就没什么问题.
