# Description
Given a collection of distinct integers, return all possible permutations.

**Example:**
```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

# Code
```python3
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        stack = []
        ret2 = []
        for i in range(len(nums)):
            ret.append([nums[i]])
        while len(ret[0]) < len(nums):
            for i in range(len(ret)):
                for j in range(len(nums)):
                    if nums[j] not in ret[i]:
                        temp = ret[i].copy()
                        temp.append(nums[j])
                        ret2.append(temp)
            ret = ret2
            ret2 = []
        return ret
```
