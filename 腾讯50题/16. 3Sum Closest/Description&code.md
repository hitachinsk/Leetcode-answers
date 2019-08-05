# Description
Given an array `nums` of n integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

**Example:**
```
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

# Code
```python3
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        ret = nums[0] + nums[1] + nums[2]
        minDistance = abs(target - ret)
        for i in range(0, len(nums) - 2):
            low, high = i + 1, len(nums) - 1
            while low < high:
                sums = nums[low] + nums[high] + nums[i]
                distance = abs(sums - target)
                if distance < minDistance:
                    minDistance = distance
                    ret = sums
                if sums < target:
                    low += 1
                elif sums > target:
                    high -= 1
                else:
                    return ret
        return ret
```
