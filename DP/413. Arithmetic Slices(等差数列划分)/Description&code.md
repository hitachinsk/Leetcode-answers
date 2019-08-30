# Description
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:
```
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
```
The following sequence is not arithmetic.
```
1, 1, 2, 5, 7
```
A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A. 

**Example:**
```
A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
```
# Code
```python3
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if A == []:
            return 0
        start = 0
        ret = 0
        while start < len(A):
            flag = False
            end = start + 1
            while end < len(A):
                if flag == False:
                    diff = A[end] - A[end - 1]
                    flag = True
                    end += 1
                else:
                    if A[end] - A[end - 1] != diff:
                        break
                    end += 1
            end -= 1
            if end == len(A) - 1:
                ret += self.calculatePartition(start, end)
                return ret
            ret += self.calculatePartition(start, end)
            start = end
            
    def calculatePartition(self, start, end):
        ret = 0
        length = end - start + 1
        for i in range(3, length + 1):
            ret += (length - i + 1)
        return ret
```
