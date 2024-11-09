# https://leetcode.com/problems/remove-linked-list-elements/description/

from typing import Any, Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next

    # def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    #     current = head
    #     while current:
    #         if current.val == val:
    #             current.next = current.next.next
    #         else:
    #             current = current.next
    #     return head
