# 100. Same Tree
# https://leetcode.com/problems/same-tree/description/
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p and q not null
        if not p and not q:
            return True

        # if p or q is null or p and q values not equal
        if (not p or not q) or (p.val != q.val):
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
