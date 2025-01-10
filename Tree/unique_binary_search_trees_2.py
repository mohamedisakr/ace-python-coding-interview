# 95. Unique Binary Search Trees II
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/

from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        if n == 1:
            return [TreeNode(1)]

        cache = {}

        def generate(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]

            if (start, end) in cache:
                return cache[(start, end)]

            ans = []
            for val in range(start, end + 1):
                left_subtrees = generate(start, val-1)
                right_subtrees = generate(val + 1, end)

                # Pre-compute lists to avoid repeated calls
                ans.extend(
                    TreeNode(val, left, right)
                    for left in left_subtrees
                    for right in right_subtrees
                )

            cache[(start, end)] = ans
            return ans

        return generate(1, n)

# old solution

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
#         if n == 0:
#             return []

#         cache = {}

#         def generate(start: int, end: int) -> List[Optional[TreeNode]]:
#             if start > end:
#                 return [None]

#             if (start, end) in cache:
#                 return cache[(start, end)]

#             ans = []

#             for val in range(start, end + 1):
#                 for left_subtree in generate(start, val-1):
#                     for right_subtree in generate(val + 1, end):
#                         root = TreeNode(val, left_subtree, right_subtree)
#                         ans.append(root)

#             cache[(start, end)] = ans
#             return ans

#         return generate(1, n)
