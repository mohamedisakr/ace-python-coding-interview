# 107. Binary Tree Level Order Traversal II
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        values = []
        q = deque([root])

        while q:
            level_size = len(q)
            level_nodes = []

            for _ in range(level_size):
                node = q.popleft()
                level_nodes.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            values.insert(0, level_nodes)

        return values
