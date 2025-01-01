# i implemented TreeNode and BinaryTree data structures for BinaryTree i implement a function
# get_sibling that take a node as an argument and return it's sibling node, none otherwise.
# BinaryTree is a rooted binary that has it's nodes value is integers

from typing import Optional


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root: TreeNode = None

    def _find_parent_and_sibling(self, current_node: TreeNode, target_node: TreeNode) -> Optional[TreeNode]:
        if current_node is None:
            return None

        if current_node.left is target_node:
            return current_node.right

        if current_node.right is target_node:
            return current_node.left

        left_result = self._find_parent_and_sibling(
            current_node.left, target_node)

        if left_result is not None:
            return left_result

        return self._find_parent_and_sibling(current_node.right, target_node)

    def get_sibling(self, node: TreeNode) -> Optional[TreeNode]:
        if self.root is None or node is self.root:
            return None
        return self._find_parent_and_sibling(self.root, node)


def main():
    tree = BinaryTree()  # Creating an empty tree
    root = TreeNode(1)
    tree.root = root
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)

    node = tree.root.left
    sibling = tree.get_sibling(node)

    if sibling:
        print(sibling.value)  # Output: 3
    else:
        print("No sibling found")


if __name__ == "__main__":
    main()

# def get_sibling(self, node: TreeNode) -> Optional[TreeNode]:
    # parent = self.get_parent(node)
    # if parent is None:
    #     return None
    # return parent.left if parent.left is not node else parent.right


# def main():
#     tree = BinaryTree()  # Creating an empty tree
#     root = TreeNode(1)
#     tree.root = root
#     tree.root.left = TreeNode(2)
#     tree.root.right = TreeNode(3)
#     node = tree.root.left
#     sib = tree.get_sibling(node)
#     print(sib.value)  # Output: 3


# if __name__ == "__main__":
#     main()

# def _find_parent(self, current_node: TreeNode, target_node: TreeNode) -> Optional[TreeNode]:
    #     if current_node is None:
    #         return None

    #     if (current_node.left is target_node) or (current_node.right is target_node):
    #         return current_node

    #     parent = self._find_parent(current_node.left, target_node)
    #     if parent is not None:
    #         return parent

    #     return self._find_parent(current_node.right, target_node)

    # def get_parent(self, node: TreeNode) -> Optional[TreeNode]:
    #     if self.root is None:
    #         return None
    #     return self._find_parent(self.root, node)
