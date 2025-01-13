# 109. Convert Sorted List to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Approach 2: Recursion + Array
        list_values = []
        current = head

        while current:
            list_values.append(current.val)
            current = current.next

        def helper(lo: int, hi: int) -> TreeNode | None:
            if lo > hi:
                return None

            m = (lo + hi) // 2
            root = TreeNode(list_values[m])
            root.left = helper(lo, m - 1)
            root.right = helper(m + 1, hi)
            return root

        return helper(0, len(list_values) - 1)

# Approach 1: Recursion + slow and fast pointers
# if not head:
#     return None

# if not head.next:
#     return TreeNode(head.val)

# def find_middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
#     slow: ListNode = head
#     fast: ListNode = head
#     prev: ListNode = None

#     while fast and fast.next:
#         prev = slow
#         slow = slow.next
#         fast = fast.next.next

#     if prev:
#         prev.next = None

#     return slow

# mid_node = find_middle_node(head)
# root = TreeNode(mid_node.val)
# root.left = self.sortedListToBST(head)
# root.right = self.sortedListToBST(mid_node.next)
# return root
