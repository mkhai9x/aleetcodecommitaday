from heapq import *
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      frequent = {}
      for num in nums:
        try:
          frequent[num] += 1
        except:
          frequent[num] = 1
      other = {}
      for num in nums:
        try:
          other[frequent[num]].add(num) 
        except:
          other[frequent[num]] = {num}
      result = []
      most_frequent = sorted(other.keys(), reverse=True)
      print(most_frequent)
      print(other)
      i = 0
      for most in most_frequent:
        for num in other[most]:
          print(most)
          result.append(num)
          i += 1
          if i == k:
            return result


      