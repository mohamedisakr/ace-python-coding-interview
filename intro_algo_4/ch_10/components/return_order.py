# The order of a tree is defined by its highest degree node.
# Eg if the tree’s highest degree is 3, then the tree has order 3.

# i want to implement a function get_order that return BinaryTree highest degree node
# BinaryTree is a rooted binary that has it's nodes value is integers

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
