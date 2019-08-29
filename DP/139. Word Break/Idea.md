刚开始我还真的没看出来这道题是DP...这道题本质上是背包问题的变体,字符串实际上相当于一定容量的背包,而词汇字典当中元素相当于一个个放在背包里面的物件,
目标就是能否从物件当中找出一个方案使得物件恰好填满背包.

对于这道题,算法如下.
- 首先对于一个字符串`s`, 初始化一个长度为`len(s) + 1`的数组`dp`,并且把`dp[0]`设置为True,其余元素设置为`False`,因为第一个元素默认为空,空元素自动满足
题意,那就是一个词汇都不拿出来.
- 然后执行外层循环`i=0:len(s)`,这一层循环的目的是使得目标数组从小到大进行增长,便于对每一个时刻的目标数组做出是否满足题意的判断
- 在执行内层循环`j=0:i+1`,`j`的目的主要是将当前目标数组分割为两段,如果第一段满足`dp[j]`为`True`并且第二段的单词也能在词汇表当中找到的话,那么就认为当前
数组是可以被分割的,设定`dp[i+1]`为`True`并退出循环,反之为`False`并继续循环
- 最后,返回`dp[len(s)]`的值为最终结果