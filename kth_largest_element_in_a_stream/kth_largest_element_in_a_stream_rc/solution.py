from typing import List
from heapq import heappop, heappush
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)
    def add(self, val: int) -> int:
        heappush(self.min_heap,val)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]



if __name__ == '__main__':
    largest = KthLargest(2, [0])
    print(largest.add(3))
    print(largest.add(5))
    print(largest.add(10))
    print(largest.add(9))
    print(largest.add(4))



