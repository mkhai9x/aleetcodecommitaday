from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        has_cyle = self.isCycle(head)
        visited = {}
        cycle_head = head
        if has_cyle:
            while cycle_head is not None:
                if cycle_head not in visited:
                    visited[cycle_head] = 1
                else:
                    return cycle_head
                cycle_head = cycle_head.next

        else:
            return None

    def isCycle(self, head: Optional[ListNode]):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False