# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/


from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive implementation


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Left->Root->Right"""
        nodes_values: list[int] = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return  # nodes_values
            inorder(node.left)
            nodes_values.append(node.val)
            inorder(node.right)

        inorder(root)
        return nodes_values


# =============================================

# from typing import Optional, List


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # iterative implementation


# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         """Left->Root->Right"""
#         nodes_values: List[int] = []
#         stack: List[Optional[TreeNode]] = []
#         current = root

#         while current or stack:
#             while current:
#                 stack.append(current)
#                 current = current.left

#             current = stack.pop()
#             nodes_values.append(current.val)
#             current = current.right

#         return nodes_values

# if root:
#     nodes_values.append(self.inorderTraversal(root.left))
#     nodes_values.append(self.inorderTraversal(root))
#     nodes_values.append(self.inorderTraversal(root.right))

# return nodes_values
