# 653. Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited_set = set()

        def search_depth_first(node):
            if node is None:
                return False

            complement = k - node.val
            if complement in visited_set:
                return True

            visited_set.add(node.val)

            return search_depth_first(node.left) or search_depth_first(node.right)

        return search_depth_first(root)
