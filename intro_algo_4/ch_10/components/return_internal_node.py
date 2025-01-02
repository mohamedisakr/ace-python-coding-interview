# implement a function for rooted binary tree that take a node as an argument and
# return true if it is a internal node, false otherwise. rooted binary tree node value
# should be integers

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root: TreeNode = None

    def is_internal(self, node: TreeNode) -> bool:
        if not node:
            return False
        return node.left is not None or node.right is not None
