from typing import List


def partition(arr: List[str], low: int, high: int, pivot: str) -> int:
  i = low - 1
  j = low
  while j < high:
    if arr[j] < pivot:
      i += 1
      arr[i], arr[j] = arr[j] , arr[i]
    elif arr[j] == pivot:
      arr[j], arr[high] == arr[high], arr[j]
      j -= 1
    j += 1
  arr[i], arr[high] = arr[high], arr[i]
  return i
    

def match_pairs(nuts: List[str], bolts: List[str], low, high) -> List[str]:
  if low < high:
    pivot = partition(nuts, low, high, bolts[high])
    partition(bolts, low, high, nuts[pivot])

    match_pairs(nuts, bolts, low, pivot - 1)
    match_pairs(nuts, bolts, pivot + 1, high)

