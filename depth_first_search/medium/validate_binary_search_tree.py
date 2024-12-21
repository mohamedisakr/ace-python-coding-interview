# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], lower: float, upper: float) -> bool:
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not validate(node.right, val, upper):
                return False
            if not validate(node.left, lower, val):
                return False
            return True

        return validate(root, float('-inf'), float('inf'))
