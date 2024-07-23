

def partition(arr, low, high, pivot):
  i = low - 1
  j = low
  while j < high: 
    if arr[j] < pivot: 
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
    elif arr[j] == pivot:
      arr[j], arr[high] = arr[high], arr[j]
      j -= 1
    j += 1
  i += 1
  arr[i], arr[high] = arr[high], arr[i]
  return i

def quicksort(arr, low, high):
  if low < high:
    pivot_index = partition(arr, low, high, arr[high])
    quicksort(arr, low, pivot_index - 1)
    quicksort(arr, pivot_index + 1, high)


arr = [10, 3, 6, 4, 7]
quicksort(arr, 0, 4)
print(arr)