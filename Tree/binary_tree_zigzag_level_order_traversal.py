# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            # Pre-allocate list with correct size
            current_level = [0] * level_size

            for i in range(level_size):
                node = queue.popleft()

                # Fill position based on direction
                position = i if left_to_right else level_size - 1 - i
                current_level[position] = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)
            left_to_right = not left_to_right

        return result


sol = Solution()
nodes_values = sol.zigzagLevelOrder(root=[3, 9, 20, None, None, 15, 7])
print(nodes_values)


# old solution
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []

#         nodes_values = []
#         q = deque([root])  # if root else []

#         while q:
#             level = []

#             for _ in range(len(q)):
#                 node = q.popleft()
#                 level.append(node.val)

#                 if node.left:
#                     q.append(node.left)

#                 if node.right:
#                     q.append(node.right)

#             level = reversed(level) if len(nodes_values) % 2 else level
#             nodes_values.append(level)

#         return nodes_values
