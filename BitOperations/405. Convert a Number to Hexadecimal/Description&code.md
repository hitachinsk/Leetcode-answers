# Description
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

**Note:**
* All letters in hexadecimal (a-f) must be in lowercase.
* The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
* The given number is guaranteed to fit within the range of a 32-bit signed integer.
* You must not use any method provided by the library which converts/formats the number to hex directly.

**Example1:**
```
Input:
26

Output:
"1a"
```

**Example2:**
```
Input:
-1

Output:
"ffffffff"
```

# Code
```python3
class Solution:
    def toHex(self, num: int) -> str:
        ret = ''
        convertTable = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        if num == 0:
            return '0'
        if num > 0:
            while num != 0:
                ret += convertTable[num % 16]
                num = num // 16
        else:
            num = 2**32 + num
            while num != 0:
                ret += convertTable[num % 16]
                num = num // 16
        return self.form(ret)
    
    def form(self, ret):
        trueRet = ""
        for i in range(len(ret) - 1, -1, -1):
            trueRet += ret[i]
        return trueRet
```
