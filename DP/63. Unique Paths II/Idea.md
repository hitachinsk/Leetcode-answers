这道题其实是之前的`Unique Paths`的变体, 输入的图不再是畅通无阻的,而是在某些`block`上面加入了实实在在的障碍物,这些障碍物的加入使得有一些之前能够走得通
的路径走不通.

考虑以下几种情况:
* 首先,如果障碍物加在了输入图的最后一列,那么在障碍物左边的所有blocks将全部是0(包括障碍物本身的block), 因为规定只能向右走或者向下走
* 其次, 如果障碍物出现在了最右边一列, 那么障碍物上方的所有blocks将全部为0, 因为这些blocks只能向下走,但是下方的道路被堵住了
* 最后, 如果障碍物出现在了其余部位,那么障碍物自身的block值将会被设定为0, 其余blocks按照正常方式计算路径多寡.

与`Unique Path`一样, 本题的DP迭代关系式为`Path(a, b) = Path(a+1, b) + Path(a, b+1)`, 然后最下面一行和最右边一列单独生成即可.
