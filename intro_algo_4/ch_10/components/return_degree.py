# i implemented TreeNode and BinaryTree data structures for BinaryTree i implement a function
# get_degree that take a node as an argument and return it's degree
# BinaryTree is a rooted binary that has it's nodes value is integers

from typing import Optional, Tuple


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

    def is_leaf(self, node: TreeNode) -> bool:
        if node is None:
            return False
        return node.left is None and node.right is None

    def get_degree(self, node: TreeNode) -> int:
        if node is None:
            return None

        # Calculate degree directly
        degree = 0

        if node.left is not None:
            degree += 1

        if node.right is not None:
            degree += 1

        return degree


def main():
    tree = BinaryTree()
    root = TreeNode(1)
    tree.root = root
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    node = tree.root
    degree = tree.get_degree(node)
    print(degree)  # Output: 2


if __name__ == "__main__":
    main()
