# Description
You are standing at position `0` on an infinite number line. There is a goal at position `target`.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination. 

**Example1:**
```
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
```
**Example2:**
```
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
```
Note:
* `target` will be a non-zero integer in the range `[-10^9, 10^9]`.

# Code
```python3
class Solution:
    def reachNumber(self, target: int) -> int:
        ret = 0
        target = abs(target)
        sums = 0
        while sums < target:
            ret += 1
            sums += ret
        if sums == target:
            return ret
        elif sums > target:
            if (sums - target)%2 == 0:
                return ret
            elif ret % 2 != 0:
                return ret + 2
            else:
                return ret + 1
```
