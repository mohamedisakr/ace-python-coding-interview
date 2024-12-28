from typing import Optional, Tuple, Type, Any
from tree_node import TreeNode
from stacks.stack import MyStack


class BinarySearchTree:
    """
    Binary Search Tree (BST) implementation.
    """

    def __init__(self):
        self._root: TreeNode = None

    def __repr__(self) -> str:
        return f'BinarySearchTree({str(self)})'

    def __str__(self) -> str:
        return TreeNode._node_str(self._root)

    def contains(self, val: Any) -> Optional[Tuple[TreeNode, TreeNode]]:
        return self._search(val)

    def _search(self, val: Any) -> Optional[Tuple[TreeNode, TreeNode]]:
        parent: TreeNode = None
        current: TreeNode = self._root

        while current:
            if current.value() == val:
                return current, parent
            elif current.value() < val:
                parent = current
                current = current.left()
            else:
                parent = current
                current = current.right()

        return None, None

    def insert(self, val: Any) -> None:
        current: TreeNode = self._root

        if current is None:
            self._root = TreeNode(val)
        else:
            while current:
                if val <= current.value():
                    if not current.left():
                        current.set_left(TreeNode(val))
                        break
                    current = current.left()
                elif val > current.value():
                    if not current.right():
                        current.set_right(TreeNode(val))
                        break
                    current = current.right()

    def delete(self, val: Any) -> None:
        if self._root is None:
            raise ValueError('Delete on an empty tree')

        current, parent = self._search(val)

        if current is None:
            raise ValueError('Value not found')
        if current.left() is None or current.right() is None:
            child = current.right() if current.left() is None else current.left()
            # The node has at most only one child
            if parent is None:
                self._root = child
            elif val <= parent.value():
                parent.set_left(val)
            else:
                parent.set_right(val)
        else:  # The node N has two children.
            # Find and remove the node M with the largest value in the left subtree of N.
            max_node, max_node_parent = current.left().find_max_in_subtree()
            if max_node_parent is None:  # M is the left child of N.
                new_node = TreeNode(max_node.value(), None, current.right())
            else:
                new_node = TreeNode(
                    max_node.value(), current.left(), current.right())
                max_node_parent.set_right(max_node.left())
            # Then  replace the node to be deleted with a new node with M.value(),
            # and the same subtrees as N.
            if parent is None:
                # The node is the root
                self._root = new_node
            elif val <= parent.value():
                parent.set_left(new_node)
            else:
                parent.set_right(new_node)

    def __iter__(self):
        """
        Iterate over the values in the BST.

        Parameters:
            None

        Functionality:
            Iterates over the values in the BST. The iteration starts at the root of the BST and
            traverses the tree using inorder traversal.
        """
        current = self._root
        stack = MyStack()
        while current is not None or len(stack) > 0:
            if current is None:
                current = stack.pop()
                yield current.value()
                current = current.right()
            else:
                while current.left() is not None:
                    stack.push(current)
                    current = current.left()
                yield current.value()
                current = current.right()
