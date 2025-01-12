# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/description/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def max_depth(current: Optional[TreeNode]) -> int:
            if not current:
                return 0

            left_depth = max_depth(current.left)
            right_depth = max_depth(current.right)

            nonlocal diameter
            diameter = max(diameter, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)

        max_depth(root)

        return diameter
