首先需要说明的是，这道题结果与`target`的正负并无关系，因为是从原点出发这样左右数组就会关于中心对称。

**例如：**

```
2=1-2+3
-2=-1+2-3
```
这样其实无论`target`的值是正的还是负的，那么到达`target`所需步数就不会改变。所以为了方便起见，将`target`变为绝对值然后再考虑从原点出发单向
运动。

其次，对于最终到达`target`的过程来说。要么是直接到达`target`点完成步骤，要么是路过`target`点然后再向左进行调整，所以对于小于`target`的情况均不予以讨论
直接让`sums`从1开始进行累加直到大于或者等于`target`为止。那么有以下几种情况。
* `sums == target` 没什么好说的，直接返回已经相加的次数就可以了
* `sums>target` 这一种情况下还可以分为如下情况。
  * `(sums - target)%2 == 0` 这种情况下，只需要把已经得到的步骤当中某一次运动反向即可。因为对于所有`x`而言，`|x-(-x)|`一定是一个偶数，而这个偶数就
  可以对`sums`进行微调使之达到`target`。而`sums`和`target`之间差值一定不会大于可调整最大偶数值（每一个步骤才差1），所以此时还是返回走的次数就可以了。
  * `(sums - target)%2 != 0` 这种情况下，需要分析已经走的步骤数`ret`的奇偶性质，`ret`为偶数，那么`ret+1`为奇数，而`sums`和`target`之间正好差
  奇数，所以可以在下一次到达；如果`ret`为奇数，那么`ret+1`为偶数，那么在下一次还是不能到达，只有在`ret+2`的时候才能到达（因为`ret+2`是奇数，可以弥补奇数
  差距）
  
本题是Leetcode简单题当中非常好的一道题，需要掌握。