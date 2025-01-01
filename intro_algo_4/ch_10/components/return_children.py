# i implemented TreeNode and BinaryTree data structures for BinaryTree i implement a function
# get_children that take a node as an argument and return it's children (left and right nodes),
# none otherwise.
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

    def get_children(self, node: TreeNode) -> Optional[Tuple[Optional[TreeNode], Optional[TreeNode]]]:
        if node is None:
            return None
        # Return a tuple of left and right children, which could be None
        return (node.left, node.right)


def main():
    tree = BinaryTree()
    root = TreeNode(1)
    tree.root = root
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    node = tree.root
    children = tree.get_children(node)
    # Output: (TreeNode(2), TreeNode(3))
    print(children)


if __name__ == "__main__":
    main()

    # def get_children(self, node: TreeNode) -> Optional[Tuple[TreeNode]]:
    #     if node is None:
    #         return None

    #     if node.left is not None and node.right is None:
    #         return node.left

    #     if node.left is None and node.right is not None:
    #         return node.right

    #     if node.left is not None and node.right is not None:
    #         return node.left, node.right
