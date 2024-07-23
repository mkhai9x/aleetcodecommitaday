
from typing import List

'''
arr1 = [1, 4, 7]
arr2 = [2, 3, 8]

result = [1, 2, 3, 4, 7, ]
'''
def sort_two_sorted_array(arr1: List[int], arr2: List[int]):
  first = second = 0
  result = []
  while first < len(arr1) and second < len(arr2) :
    if arr1[first] < arr2[second]:
      result.append(arr1[first])
      first += 1 
    elif arr1[first] > arr2[second]:
      result.append(arr2[second])
      second += 1
  if first == len(arr1):
    result.extend(arr2[second:])
  if second == len(arr2):
    result.extend(arr1[first:])
  return result





def merge(arr: List[int], low: int, high: int):
  if low == high:
    return [arr[low]]
  
  mid = (low + high)//2

  first_half = merge(arr, low, mid)
  second_half = merge(arr, mid + 1, high)
  result = sort_two_sorted_array(first_half, second_half)
  return result


print(merge([1, 10, 3, 5, 100, 101], 0, 5))

