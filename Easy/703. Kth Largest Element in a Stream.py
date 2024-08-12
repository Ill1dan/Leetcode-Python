from heapq import heapify, heappop, heappush

class KthLargest(object):

    def __init__(self, k, nums):
        self.k, self.minheap = k, nums
        heapify(self.minheap)
        while len(self.minheap) > k:
            heappop(self.minheap)

    def add(self, val):
        heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heappop(self.minheap)

        return self.minheap[0]
