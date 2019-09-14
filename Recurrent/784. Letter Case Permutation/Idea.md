本题又是一道生成树的题目,生成树最大的好处就是可以按照前后顺序遍历所有情况从而达到不重不漏.

本题算法如下:
- 首先,从前到后遍历数组,如果遇到数字就将数字加入到字符串当中,直到遇到第一个字母
- 如果数组越界,表明原数组无字母,直接返回就好,反之将字母原来形式和转变大小写的形式生成的两个字符串分别加入到结果数组当中
- 从当前所以向后遍历数组,将结果数组所有的字符串取出,如果遍历得到的是字母,就将字母原来形式和转变大小写的形式生成的两个字符串分别加入到暂存数组当中,
反之就将数组加上数字存入暂存数组当中
- 将结果数组与暂存数组交换位置
- 返回结果数组