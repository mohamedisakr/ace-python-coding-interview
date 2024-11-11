# https://leetcode.com/problems/add-two-numbers/description
# Definition for singly-linked list.
from typing import Any, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            current.next = ListNode(carry % 10)
            carry //= 10
            current = current.next

        return dummy.next


# l1 = [2, 4, 3]
head1 = ListNode(2)
head1.next = ListNode(4)
head1.next.next = ListNode(3)

# l2 = [5, 6, 4]
head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)

sol = Solution()
sum_num = sol.addTwoNumbers(head1, head2)
print(sum_num)
