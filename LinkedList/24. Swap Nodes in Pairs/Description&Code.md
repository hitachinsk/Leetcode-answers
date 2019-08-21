# Description
Given a linked list, swap every two adjacent nodes and return its head.

You may **not** modify the values in the list's nodes, only nodes itself may be changed.

**Example:**
```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```

# Code
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is  None:
            return head
        p = head
        q = head.next
        s = None
        while p is not None and q is not None:
            if s is not None:
                s.next = q
            p.next = p.next.next
            q.next = p
            if p == head:
                head = q
            s = p
            try:
                p = p.next.next
                q = q.next.next
            except:
                break
            temp = p
            p = q
            q = temp
        return head
```
