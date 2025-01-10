# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None

            m = (lo + hi) // 2
            root = TreeNode(nums[m])
            root.left = build_tree(lo, m - 1)
            root.right = build_tree(m + 1, hi)

            return root

        return build_tree(0, len(nums) - 1)
