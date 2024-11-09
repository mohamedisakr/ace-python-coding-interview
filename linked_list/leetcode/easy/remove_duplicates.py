# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
from typing import Any, Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    # def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     visited_nodes = {}
    #     previous = None
    #     current = head

    #     while current is not None:
    #         if current.val in visited_nodes:
    #             previous.next = current.next
    #         else:
    #             visited_nodes[current.val] = True
    #             previous = current
    #         current = current.next
