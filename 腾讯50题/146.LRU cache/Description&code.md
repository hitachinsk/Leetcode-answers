# Description
 Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
```
LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

# Code
**This code is out of the time limit in Leetcode!(not passed)**
```
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        

class LinkList:
    def __init__(self):
        self.head = None
        self.rear = None
        
    def append(self, key, val):
        if self.head == None:
            self.head = Node(key, val)
            self.rear = self.head
        else:
            self.rear.next = Node(key, val)
            self.rear = self.rear.next
            
    def delete(self):
        if self.head == None:
            return
        if self.head == self.rear:
            self.head = None
            self.rear = None
        else:
            p = self.head
            self.head = self.head.next
            p.next = None
            
    def __len__(self):
        ret = 0
        p = self.head
        if p == None:
            return 0
        while p != None:
            ret += 1
            p = p.next
        return ret
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.link = LinkList()

    def get(self, key: int) -> int:
        p = self.link.head
        if p == None:
            return -1
        if p.next == None:
            if p.key == key:
                return p.val
        if p.key == key:
            self.link.head = self.link.head.next
            p.next = None
            self.link.rear.next = p
            self.link.rear = self.link.rear.next
            return p.val
        while p.next != None:
            if p.next.key == key:
                ret = p.next.val
                if p.next.next == None:
                    return ret
                pointer = p.next
                p.next = p.next.next
                self.link.rear.next = pointer
                self.link.rear = self.link.rear.next
                pointer.next = None
                return ret
            p = p.next
        return -1
        
    def put(self, key: int, value: int) -> None:
        p = self.link.head
        if self.capacity == 0:
            return
        if p == None:
            self.link.append(key, value)
            return
        if p.next == None:
            if p.key == key:
                p.val = value
            else:
                if len(self.link) == self.capacity:
                    self.link.delete()
                self.link.append(key, value)
            return
        if p.key == key:
            p.val = value
            self.link.head = self.link.head.next
            p.next = None
            self.link.rear.next = p
            self.link.rear = self.link.rear.next
            return
        while p.next != None:
            if p.next.key == key:
                p.next.val = value
                if p.next.next == None:
                    return
                
                pointer = p.next
                p.next = p.next.next
                self.link.rear.next = pointer
                self.link.rear = self.link.rear.next
                pointer.next = None
                return
            p = p.next
        if len(self.link) == self.capacity:
            self.link.delete()
        self.link.append(key, value)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```
