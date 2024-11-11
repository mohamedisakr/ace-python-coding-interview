# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
from typing import Any, Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n+1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next


my_head = ListNode(1)
first = ListNode(2)
my_head.next = first
second = ListNode(3)
first.next = second
third = ListNode(4)
second.next = third
fourth = ListNode(5)
third.next = fourth
#

sol = Solution()
# the_head = sol.removeNthFromEnd(my_head, 2)
size = sol.removeNthFromEnd(my_head, 2)
print(f'linked list size: {size}')
