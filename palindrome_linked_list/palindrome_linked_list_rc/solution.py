# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        head_second_half = self.reverse(slow)
        head_second_half_reverse = head_second_half
        while head_second_half is not None and head is not None:
            if head.val != head_second_half.val:
                break
            head = head.next
            head_second_half = head_second_half.next
        self.reverse(head_second_half_reverse)
        if  head_second_half is None:
            return True
        return False
    def reverse(self,head):
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev