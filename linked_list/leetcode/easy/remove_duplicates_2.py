# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
from typing import Any, Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            # If current node is a start of duplicates sublist
            # skip all nodes with the same value.
            if head.next and head.val == head.next.val:
                # Move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip all duplicates
                prev.next = head.next
            else:
                # No duplicates detected, move predecessor
                prev = prev.next
            # Move forward
            head = head.next

        return dummy.next


# [1, 2, 3, 3, 4, 4, 5]
my_head = ListNode(1)
first = ListNode(2)
my_head.next = first
second = ListNode(3)
first.next = second
third = ListNode(3)
second.next = third
fourth = ListNode(4)
third.next = fourth
fiveth = ListNode(4)
fourth.next = fiveth
sixth = ListNode(5)
fiveth.next = sixth

sol = Solution()
the_head = sol.deleteDuplicates(my_head)

current = my_head
while current:
    print(current.val, sep=',')
    current = current.next
