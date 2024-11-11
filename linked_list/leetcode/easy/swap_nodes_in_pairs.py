# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/description/

from typing import Any, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous, current = dummy, head

        while current and current.next:
            # save the next pair of nodes
            next_pair = current.next.next
            second = current.next

            # reverse the current pair of nodes
            second.next = current
            current.next = next_pair
            previous.next = second

            # update pointers
            previous = current
            current = next_pair

        return dummy.next


def swap(arr: Optional[list]):
    n = len(arr)
    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


# sol = Solution()
arr = [1, 2, 3, 4]
print(swap(arr))  # [2, 1, 4, 3]
