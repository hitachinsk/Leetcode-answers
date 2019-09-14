# Description
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.
```
Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
```
**Note:**
- `S` will be a string with length between `1` and `12`.
- `S` will consist only of letters or digits.

# Code
```python3
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if S == '':
            return ['']
        ret = []
        stack = []
        i = 0
        temp = ''
        while i < len(S) and not S[i].isalpha():
            temp += S[i]
            i += 1
        try:
            ret.append(temp + S[i])
            ret.append(temp + self.convert(S[i]))
        except:
            return [temp]
        for j in range(i+1, len(S)):
            if S[j].isalpha():
                for each in ret:
                    stack.append(each + S[j])
                    stack.append(each + self.convert(S[j]))
            else:
                for each in ret:
                    stack.append(each + S[j])
            ret = stack
            stack = []
        return ret
        
    def convert(self, char):
        if char == char.upper():
            return char.lower()
        return char.upper()
```
