import heapq
import random

class TopHeap():
	def __init__(self, array, k):
		self.array = []
		self.k = k
		for num in array:
			self.push(num)

	def push(self, val):
		if len(self.array) < self.k:
			heapq.heappush(self.array, val)
		else:
			topk_small = self.array[0]
			if val > topk_small:
				heapq.heapreplace(self.array, val)

	def topK(self):
		return [x for x in reversed([heapq.heappop(self.array) for x in range(len(self.array))])]

# 在heapq当中未实现大顶堆的代码,但是大顶堆可以通过用户将输入元素变为负数之后再构建小顶堆的操作等效进行
class SmallHeap():
	def __init__(self, array, k):
		self.array = []
		self.k = k
		for num in array:
			self.push(num)

	def push(self, val):
		if len(self.array) < self.k:
			heapq.heappush(self.array, -val)
		else:
			topk_big = self.array[0]
			if -val > topk_big:
				heapq.heapreplace(self.array, -val)

	def btmK(self):
		return [-x for x in reversed([heapq.heappop(self.array) for x in range(len(self.array))])]


if __name__ == '__main__':
	a = [1,5,9,2,6,8,4,7,4]
	sh = TopHeap(a, 3)
	print(sh.topK())
