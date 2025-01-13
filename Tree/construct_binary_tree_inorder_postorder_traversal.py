# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = {v: i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return None

            root = TreeNode(postorder.pop())
            idx = inorder_indices[root.val]
            root.right = helper(idx + 1, r)
            root.left = helper(l, idx - 1)
            return root

        return helper(0, len(inorder) - 1)

# O(n^2)
        # if not inorder:
        #     return None

        # root = TreeNode(postorder.pop())
        # idx = inorder.index(root.val)

        # root.right = self.buildTree(inorder[idx+1:], postorder)
        # root.left = self.buildTree(inorder[:idx], postorder)
        # return root
