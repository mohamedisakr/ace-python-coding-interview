# 112. Path Sum
# https://leetcode.com/problems/path-sum/description/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive approach


class Solution:
    # Root -> Left -> Right
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if root.val == targetSum and root.left is None and root.right is None:
            return True

        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


# from typing import Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# # iterative approach
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False

#         stack = [(root, targetSum - root.val)]

#         while stack:
#             node, curr_sum = stack.pop()
#             if not node.left and not node.right and curr_sum == 0:
#                 return True
#             if node.left:
#                 stack.append((node.left, curr_sum - node.left.val))
#             if node.right:
#                 stack.append((node.right, curr_sum - node.right.val))

#         return False

# def is_leaf(node: TreeNode):
#     return node.left is None and node.right is None
    # current = root
    # total = 0

    # if is_leaf(current) is False:
    #     if current.val == targetSum:
    #         return True
    #     total -= current.val
