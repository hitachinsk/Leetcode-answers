# Description
Let's define a function `f(s)` over a non-empty string `s`, which calculates the frequency of the smallest character in `s`. For example, if `s = "dcce"` then `f(s) = 2` because the smallest character is `"c"` and its frequency is 2.
Now, given string arrays `queries` and `words`, return an integer array `answer`, where each `answer[i]` is the number of words such that `f(queries[i])` < `f(W)`, where `W` is a word in `words`.

**Example1:**
```
Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
```
**Example2:**
```
Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
```
**Constraints:**
- `1 <= queries.length <= 2000`
- `1 <= words.length <= 2000`
- `1 <= queries[i].length, words[i].length <= 10`
- `queries[i][j]`, `words[i][j]` are English lowercase letters.

# Code
```python3
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ret = []
        cache = []
        for i in range(len(words)):
            cache.append(self.function(words[i]))
        for i in range(len(queries)):
            length = self.function(queries[i])
            k = 0
            for j in range(len(cache)):
                if length < cache[j]:
                    k += 1
            ret.append(k)
        return ret
                   
    def function(self, s):
        dic = {}
        min_char = 'z'
        for i in range(len(s)):
            if s[i] < min_char:
                min_char = s[i]
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        return dic[min_char]
```
