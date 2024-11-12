# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/description

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # determine if there is a cycle
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                # There is a cycle, now find the start of the cycle
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None
