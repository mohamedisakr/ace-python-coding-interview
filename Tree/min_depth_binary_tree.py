# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

from collections import deque
from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = deque([(root, 1)])

        while q:
            node, depth = q.popleft()

            # If it's a leaf node, return the current depth
            if not node.left and not node.right:
                return depth

            if node.left:  # add left child to the queue, if it exist
                q.append((node.left, depth + 1))

            if node.right:  # add right child to the queue, if it exist
                q.append((node.right, depth + 1))


# if root is None:
#     return 0
# if root.left is None:
#     return 1 + self.minDepth(root.right)
# if root.right is None:
#     return 1 + self.minDepth(root.left)
# return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
