# Description
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

# Code
```python3
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = ['(']
        stack = []
        counterStore = [(1, 0)]
        counterStoreStack = []
        for i in range(1, 2*n):
            for j in range(len(res)):
                counter = counterStore[j]
                counterPointer = counter[0]
                if counterPointer == n:
                    stack.append(res[j] + ')')
                    counterStoreStack.append((counter[0], counter[1]+1))
                else:
                    stack.append(res[j] + '(')
                    counterStoreStack.append((counter[0]+1, counter[1]))
                    if counter[0] >= counter[1]+1:
                        stack.append(res[j] + ')')
                        counterStoreStack.append((counter[0], counter[1]+1))
            res = stack
            stack = []
            counterStore = counterStoreStack
            counterStoreStack = []
        return res
```
