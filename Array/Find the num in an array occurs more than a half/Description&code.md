# Description
数组当中有一个数字出现次数超过了数组长度的一半,要求找到这个数字且时间复杂度为O(n), 空间复杂度为O(1)

# Code
```java
public class FindMoreHalfNums {
    public static void main(String[] args) {
        int [] test = new int [] {4,6,8,4,4,4,4,4,6,2,4,5} ;
        Solution sol = new Solution(test) ;
        System.out.println(sol.solution());
    }
}

class Solution {
    private int [] array;
    public Solution (int [] array) {
        this.array = array ;
    }
    /**
     * No.2 solution
     * @return value which occurs more than a half 
     */
    public int solution() {
        int times = 0;
        int num = 0;
        boolean flag = false;
        for (int i = 0; i < this.array.length; i ++) {
            if (flag == false) {
                flag = true ;
                num = this.array[i] ;
                times = 1;
            } else {
                if (this.array[i] == num) {
                    times ++ ;
                    if (times > this.array.length / 2) {
                        return num ;
                    }
                } else {
                    times -- ;
                    if (num < 0) {
                        flag = false ;
                    }
                }
            }
        }
        return num ;
    }
}
```
