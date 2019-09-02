# Description
Design a class to find the **k**th largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your `KthLargest` class will have a constructor which accepts an integer `k` and an integer array nums, which contains initial elements from the stream. For each call to the method `KthLargest.add`, return the element representing the `kth` largest element in the stream.

**Example:**
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

**Note:**
You may assume that `nums`' length ≥ `k-1` and `k` ≥ `1`

# Code
```python3
# 2.小顶堆
import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        heapq.heapify(self.pool)
        self.k = k
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
```

```python3
# 自己实现的小顶堆,最后一个巨长的例子失败了...
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.smallTopHeap = []
        self.constructHeap()
        print(len(self.smallTopHeap))

    def add(self, val: int) -> int:
        self.insertElems(val)
        return self.smallTopHeap[0]
    
    def constructHeap(self):
        for i in range(len(self.nums)):
            self.insertElems(self.nums[i])
        
    def insertElems(self, elem):
        if len(self.smallTopHeap) < self.k:
            self.smallTopHeap.append(elem)
            self.siftUp()
        else:
            if elem <= self.smallTopHeap[0]:
                pass
            else:
                self.smallTopHeap[0] = elem
                self.siftDown(self.smallTopHeap, 0, len(self.smallTopHeap))
    
    def siftDown(self, array, start, end):
        i, j = start, 2 * start + 1
        temp = array[i]
        while j < end:
            if j+1 < end and array[j] > array[j+1]:
                j += 1
            if temp > array[j]:
                array[i] = array[j]
            else:
                break
            i = j
            j = 2 * i + 1
        array[i] = temp
    
    def siftUp(self):
        i = len(self.smallTopHeap) - 1
        j = i // 2
        temp = self.smallTopHeap[i]
        while j >= 0 and i > 0:
            if temp < self.smallTopHeap[j]:
                self.smallTopHeap[i] = self.smallTopHeap[j]
            else:
                break
            i = j
            j = i // 2
        self.smallTopHeap[i] = temp
```
