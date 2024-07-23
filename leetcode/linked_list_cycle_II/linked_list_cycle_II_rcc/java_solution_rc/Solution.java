class ListNode {
    int val;
    ListNode next;
    ListNode(int x){
        val = x;
        next = null;
    }
}

public class Solution {
    public ListNode detectCycle(ListNode head) {
        int cycleLength = this.hasCycle(head);
        if (cycleLength < 0) return null;
        ListNode fast = head, slow = head;
        while (cycleLength > 0) {
            fast = fast.next;
            cycleLength--;
        }
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;

        }
        return slow;



    }

    public int hasCycle (ListNode head){
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if (fast == slow){
                int cycleLength = 0;
                do {
                    fast = fast.next;
                    cycleLength++;

                } while (fast != slow);
                return cycleLength;
            }
        }
        return -1;


    }
}
