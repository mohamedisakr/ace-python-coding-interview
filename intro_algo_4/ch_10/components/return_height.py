# Maximum Depth or Height of Binary Tree
# Given a binary tree, the task is to find the maximum height of the tree.
# The height of the tree is the number of edges in the tree from the root
# to the deepest node.
from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.value})"

    def __str__(self):
        return f"({self.value})"


class BinaryTree:
    def __init__(self):
        self.root: TreeNode = None

    # depth-first search (DFS) approach.
    def height(self) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left_side = dfs(node.left)
            right_side = dfs(node.right)

            return 1 + max(left_side, right_side)

        return dfs(self.root)

    # breadth-first search (BFS) approach.
    # def height(self) -> int:
    #     if self.root is None:
    #         return 0

    #     q = deque([self.root])
    #     hi = 0

    #     while q:
    #         level_size = len(q)

    #         for _ in range(level_size):
    #             current = q.popleft()

    #             if current.left:
    #                 q.append(current.left)

    #             if current.right:
    #                 q.append(current.right)

    #         hi += 1

    #     return hi-1


if __name__ == "__main__":

    # Representation of the input tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    tree = BinaryTree()
    tree.root = TreeNode(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    print(tree.height())
