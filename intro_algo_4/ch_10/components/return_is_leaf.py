# implement a function for rooted binary tree that take a node as an argument and
# return true if it is a leaf node, false otherwise. rooted binary tree node value
# should be integers

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root: TreeNode = None

    def is_leaf(self, node: TreeNode) -> bool:
        if node is None:
            return False
        return node.left is None and node.right is None


def main():
    tree = BinaryTree()  # Creating an empty tree
    root = TreeNode(1)
    tree.root = root
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    leaf_node = tree.root.left
    print(tree.is_leaf(leaf_node))  # Output: True
    print(tree.is_leaf(tree.root))  # Output: False


if __name__ == "__main__":
    main()

# # Example usage:
# tree = BinaryTree()  # Creating an empty tree
# root = TreeNode(1)
# tree.root = root
# tree.root.left = TreeNode(2)
# tree.root.right = TreeNode(3)
# leaf_node = tree.root.left

# print(tree.is_leaf(leaf_node))  # Output: True
# print(tree.is_leaf(tree.root))  # Output: False
