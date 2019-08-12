# Description
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
```
2->abc  
3->def  
4->ghi  
5->jkl  
6->mno  
7->pqrs  
8->tuv  
9->wxyz
```
**Example:**
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```
**Note:**

Although the above answer is in lexicographical order, your answer could be in any order you want.

# Code
```python3
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        sourceRet = []
        targetRet = []
        mapping = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        for i in range(len(digits)):
            mapStr = mapping[int(digits[i]) - 2]
            if i % 2 == 0:
                ret = sourceRet
                otherRet = targetRet
            else:
                ret = targetRet
                otherRet = sourceRet
            if i == 0:
                for alpha in mapStr:
                    otherRet.append(alpha)
            while ret != []:
                temp = ret.pop()
                for each in mapStr:
                    otherRet.append(temp + each)
        if sourceRet != []:
            return sourceRet
        return targetRet
```
