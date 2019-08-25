# Description
Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.
After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of `ListNode` objects.)

**Example 1:**
```
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
```
**Example 2:**
```
Input: head = [1,2,3,-3,4]
Output: [1,2,4]
```
**Example 3:**
```
Input: head = [1,2,3,-3,-2]
Output: [1]
```
**Constraints:**
- The given linked list will contain between `1` and `1000` nodes.
- Each node in the linked list has `-1000 <= node.val <= 1000.`
# Code
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        if head.next == None:
            if head.val == 0:
                return None
            return head
        while True:
            a = self.judgeList(head)
            if a == None:
                return head
            p, q  = a
            if p == head and q == None:
                head = head.next
            elif p == head and q != None:
                head = q.next
            elif p != head and q == None:
                h = head
                while h.next != p:
                    h = h.next
                h.next = h.next.next
            elif p != head and q != None:
                h = head
                while h.next != p:
                    h = h.next
                h.next = q.next
            
    def judgeList(self, head):
        p = head
        while p != None:
            sumAll = p.val
            if sumAll == 0:
                return p, None
            q = p.next
            while q != None:
                sumAll += q.val
                if sumAll == 0:
                    return p, q
                q = q.next
            p = p.next
        return None
```
