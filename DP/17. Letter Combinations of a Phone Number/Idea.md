很显然,本题考验的是排列组合的能力,稍有不慎就会超时.

其实解决排列组合题目的一个方法就是将得到的结果进行动态增加.例如本题,如果输入为`28`的话,那么就会出现如下的结果增长情况(其实是一张图)
```
     a     b     c
    /|\   /|\   /|\
   t u v t u v t u v
````
如果再输入其余号码的话,就在每一个t,u,v底下再进行增加.

本题首先初始化了两个数组`sourceRet`以及`targetRet`,这两个数组主要是用作搬运数据的时候使用,当操作的`digits`子元素为偶数(从0开始)增长结果
由`sourceRet`向`targetRet`进行搬运,如果为奇数则是反方向搬运.这样做的好处是节省清空数组的时间,然后对于每一次搬运都将搬运源数组当中所有元素逐一取出
然后与新增长的元素拼接成为一个新的数组存向目标数组.由于最终一定会有一个数组为空,那么返回结果的时候返回那个不空数组就可以了.

下面是异常处理:如果输入为空则不用判断直接返回空数组就可以了.如果是第一次搬运一定要注意一点,由于此时源数组没有元素,如果还是采用全部取出的方式那么就会
导致直接跳过循环不能存入结果的情况发生.此时就需要进行额外判断并强制向目标数组写入映射字符串的每个字符.
