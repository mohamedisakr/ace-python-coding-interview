# i want to implement a function for rooted binary tree that take a node as an argument and return
# its parent if its parent exists, none otherwise.
# rooted binary tree node value should be integers

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = TreeNode(value)
        return self.root

    def add_child(self, parent: TreeNode, child_value, is_left):
        if parent is None:
            return None

        child = TreeNode(child_value)

        if is_left:
            parent.left = child
        else:
            parent.right = child

        child.parent = parent

        return child

    def get_parent(self, node):
        return node.parent


# Example usage:
binary_tree = BinaryTree()
root = binary_tree.set_root(1)
child1 = binary_tree.add_child(root, 2, is_left=True)
child2 = binary_tree.add_child(root, 3, is_left=False)

print(binary_tree.get_parent(child1).value)  # Output: 1
print(binary_tree.get_parent(root))          # Output: None
