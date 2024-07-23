# Data structure need to learn know

- Priority queue

  what is heaps ?

  what is a priority queue ?

Heaps are **concrete** data structures that are used to implement priority queues.

The priority queue abstract data structure, for example, supports three operations:

1. `is_empty` checks whether the queue is empty
2. `add_element` adds an element to the queue
3. `pop_element` pops the element with the highest **priority**

There are two different conventions for defining the priority of an element:

1. The _largest_ element has the highest priority
1. The _smallest_ element has the highest priority

In Python, the `heapq` module is used to implement priority queues. And it uses the **second convention**.

## Time complexity and Space complexity

The heap implementation of the priority queue guarantees that both pushing and popping elements are **O(log n)**.

For push, it takes **O(log n)** time.

For pop, it takes **O(log n)** time.

## Implementation of Heaps

A heap implements a priority queue as a **complete binary tree**.

Here is an example of a **complete binary tree**:

![complete binary tree](https://realpython.com/cdn-cgi/image/width=441,format=auto/https://files.realpython.com/media/heap-tree.4b4413ff133c.png)

In a heap tree, the value in a node is always smaller than both of its children. This is called the **heap property**.
Different than binary search tree, in which only the left node will be smaller than the value of its parent.

The algorithms for pushing and popping rely on temporarily violating the heap property, then fixing the heap property
through comparisons and replacements up or down a single branch.

## Uses of Priority Queue

- Getting the three most popular blog posts from hit data
- Finding the fastest way to get from one point to other
- Predicting which bus will be the first to arrive at a station based on arrival frequency

## Heaps as Lists in the Python `heapq` Module

Because it is a _concrete_ binary tree, it can be implemented as a list.

There are three rules that determine the relationship between the elements at the index `k` and its surrounding elements:

1. Its first child is at index `2k + 1`
2. Its second child is at index `2k + 2`
3. Its parent is at index `(k - 1)//2`

Note: All node must have a parent if it has a child. If `2k` is beyond the end of list, then the element does not have any children.

The heap property means that if `h` is a heap, then the following will never be `False`:

```
h[k] <= h[2*k +1] and h[k] <= h[2*k + 2]
```

## Basic Operations

```Python
import heapq

a = [3, 5, 1, 2, 6, 8, 7]

heapq.heapify(a) # Turn the list a to a heap

print(a) # [1, 2, 3, 5, 6, 8, 7]
```

Note: `heapify()` modifies the list in place, but does not sort it. A heap does not have to be sorted, but a sorted list does satisfy the heap property.

To pop the smallest element from the heap:

```Python
import heapq

a = [3, 5, 1, 2, 6, 8, 7]

heapq.heapify(a) # Turn the list a to a heap

smallest = heapq.heappop(a) # 1
```

The function return the first element, `1`, and preserves the heaps property on `a`.

To push an element to the heap:

```Python
import heapq

a = [3, 5, 1, 2, 6, 8, 7]

heapq.heapify(a) # Turn the list a to a heap

smallest = heapq.heappush(a, 4) # 1
```

The Python `heapq` module also provides the following methods:

1. `heapreplace()` is equivalent to `heappop()` followed by `heappush()`
2. `heappushpop()` is equivalent to `heappush()` followed by `heappop()`

Since priority queues are so often used to merged sorted sequences, the Python `heapq` module
has ready-made function `merge()`

## Problem Heaps Can Solve

Heaps are good for incrementally merging sorted sequences. Two applications for heaps that you have already considered are

- Periodic tasks
- Merging log files

Heaps can also help identify the top `n` or bottom `n` things. The Python `heapq` module has high-level functions that implements this behavior.

For examples, this code gets as input the times from the women's 100 meters final at the 2015 Summer Olympics and prints the medalists, or the top three finishers:

```Python
import heapq
results="""\
Christania Williams      11.80
Marie-Josee Ta Lou       10.86
Elaine Thompson          10.71
Tori Bowie               10.83
Shelly-Ann Fraser-Pryce  10.86
English Gardner          10.94
Michelle-Lee Ahye        10.92
Dafne Schippers          10.90
"""
top_3 = heapq.nsmallest(
    3, results.splitlines(), key=lambda x: float(x.split()[-1])
)
print("\n".join(top_3))


```

## TODO:

- Try to implement priority queues

## References

- https://realpython.com/python-heapq-module/#what-are-heaps
