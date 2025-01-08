# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from collections import deque
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # method 1 - iterative breadth-first search (BFS) approach.
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        level = 0
        q = deque([root])

        while q:
            for _ in range(len(q)):
                current = q.popleft()
                if current.left:
                    q.append(current.left)

                if current.right:
                    q.append(current.right)

            level += 1

        return level

# =======================================================================

    # method 2 - iterative depth-first search (DFS) approach.
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if root is None:
    #         return 0

    #     level = 0
    #     stack = [[root, 1]]

    #     while stack:
    #         node, depth = stack.pop()
    #         if node:
    #             level = max(level, depth)
    #             stack.append([node.left, depth+1])
    #             stack.append([node.right, depth+1])

    #     return level

# =======================================================================

    # method 3 - recursive depth-first search (DFS) approach.
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if root is None:
    #         return 0

    #     left_height = self.maxDepth(root.left)
    #     right_height = self.maxDepth(root.right)

    #     return 1 + max(left_height, right_height)
