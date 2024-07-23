from typing import List
from heapq import heappush, heappop
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return
        min_heap = []
        for min_list in lists:
            curr = min_list
            while curr:
                heappush(min_heap, (curr.val))
                curr = curr.next
        head = ListNode(0)
        point = ListNode(0)
        head.next = point
        head = head.next

        while min_heap:
            val = heappop(min_heap)
            point.next = ListNode(val)
            point = point.next

        return head.next