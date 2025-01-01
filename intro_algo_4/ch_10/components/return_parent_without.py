# Yes, we can still implement the same functionality without the parent variable
# in the TreeNode class, but we will need to traverse the tree to find the parent node.
# Here's an example implementation:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = TreeNode(value)
        return self.root

    def add_child(self, parent, child_value, is_left=True):
        if parent is None:
            return None
        child = TreeNode(child_value)
        if is_left:
            parent.left = child
        else:
            parent.right = child
        return child

    def find_parent(self, current_node, target_node):
        """recursively traverses the tree to find the parent of the target node.
        using Depth-First Search (DFS) traversal algorithm. Specifically, 
        it performs a pre-order traversal where it checks the current node, 
        then recursively checks the left subtree, followed by the right subtree.
        """
        if current_node is None:
            return None
        # Check if the current node is the parent of the target node.
        if (current_node.left is target_node) or (current_node.right is target_node):
            return current_node
        # Recursively search the left subtree for the parent.
        parent = self.find_parent(current_node.left, target_node)
        if parent is not None:
            return parent
        # If not found in the left subtree, recursively search the right subtree for the parent.
        return self.find_parent(current_node.right, target_node)

    def get_parent(self, node):
        if self.root is node:
            return None
        return self.find_parent(self.root, node)


# Example usage:
binary_tree = BinaryTree()
root = binary_tree.set_root(1)
child1 = binary_tree.add_child(root, 2, is_left=True)
child2 = binary_tree.add_child(root, 3, is_left=False)

print(binary_tree.get_parent(child1).value)  # Output: 1
print(binary_tree.get_parent(child2).value)  # Output: 1
print(binary_tree.get_parent(root))          # Output: None
