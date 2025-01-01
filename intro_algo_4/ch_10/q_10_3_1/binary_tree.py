from typing import Dict, Optional, List, Tuple
from node import TreeNode


class BinaryTree:
    def __init__(self):
        self.nodes = {}

    def add_node(self, index, key, left_index=None, right_index=None):
        # Add the node if it doesn't exist
        if index not in self.nodes:
            self.nodes[index] = TreeNode(key)

        node = self.nodes[index]

        # Add left child
        if left_index is not None:
            if left_index not in self.nodes:
                self.nodes[left_index] = TreeNode(None)
            node.left = self.nodes[left_index]

        # Add right child
        if right_index is not None:
            if right_index not in self.nodes:
                self.nodes[right_index] = TreeNode(None)
            node.right = self.nodes[right_index]

    def build_tree(self, data):
        for index, key, left, right in data:
            self.add_node(index, key, left, right)

    def display_in_order(self, root_index):
        if root_index not in self.nodes:
            return "Root not found in tree."

        def in_order_traversal(node):
            if node is not None:
                in_order_traversal(node.left)
                print(node.key, end=' ')
                in_order_traversal(node.right)

        root = self.nodes[root_index]
        in_order_traversal(root)
        print()  # Newline for better readability

    # def display(self, root_index):
    #     if root_index not in self.nodes:
    #         return "Root not found in tree."

    #     def display_helper(node, level=0):
    #         if node is not None:
    #             display_helper(node.right, level + 1)
    #             print(' ' * 4 * level + '->', node.key)
    #             display_helper(node.left, level + 1)

    #     root = self.nodes[root_index]
    #     display_helper(root)


if __name__ == "__main__":
    data = [
        (1, 17, 8, 9),
        (2, 14, None, None),
        (3, 12, None, None),
        (4, 20, 10, None),
        (5, 33, 2, None),
        (6, 15, 1, 4),
        (7, 28, None, None),
        (8, 22, None, None),
        (9, 13, 3, 7),
        (10, 25, None, 5)
    ]

    binary_tree = BinaryTree()
    binary_tree.build_tree(data)
    binary_tree.display_in_order(6)  # Root node with index 6


# class BinaryTree:
#     def __init__(self, data, root_index=None):
#         self.data = data
#         self.nodes = {}
#         self.root_index = root_index

#     # def populate(self, data):

#     def get_node(self, index):
#         if index is None:
#             return None
#         if index not in self.nodes:
#             key, left, right = self.get_attributes(index)
#             self.nodes[index] = TreeNode(key)
#             self.nodes[index].left = self.get_node(left)
#             self.nodes[index].right = self.get_node(right)
#         return self.nodes[index]

#     def get_attributes(self, index):
#         for idx, key, left, right in self.data:
#             if idx == index:
#                 return key, left, right
#         return None, None, None

#     @property
#     def root(self):
#         if self.root_index is None:
#             raise ValueError("Root index is not set.")
#         return self.get_node(self.root_index)

#     def inorder(self) -> None:
#         def _inorder(node: Optional[TreeNode]) -> None:
#             if node:
#                 _inorder(node.left)
#                 print(f"({node.index}) {node.key}")
#                 _inorder(node.right)

#         if self.root_index:
#             _inorder(self.root_index)


# data = [
#     (1, 17, 8, 9),
#     (2, 14, None, None),
#     (3, 12, None, None),
#     (4, 20, 10, None),
#     (5, 33, 2, None),
#     (6, 15, 1, 4),
#     (7, 28, None, None),
#     (8, 22, None, None),
#     (9, 13, 3, 7),
#     (10, 25, None, 5)
# ]

# binary_tree = BinaryTree(data, root_index=6)
# binary_tree.inorder()

# dot = binary_tree.visualize()
# dot.render('binary_tree', format='png', view=True)

# def visualize(self):
#     def add_nodes_edges(graph, node, parent=None):
#         if node:
#             graph.node(str(node.key))
#             if parent:
#                 graph.edge(str(parent.key), str(node.key))
#             add_nodes_edges(graph, node.left, node)
#             add_nodes_edges(graph, node.right, node)

#     dot = graphviz.Digraph()
#     add_nodes_edges(dot, self.root)
#     return dot

# ==================================================================

# the old implementation
# import graphviz

# class BinaryTree:
#     def __init__(self) -> None:
#         self._root: Optional[TreeNode] = None
#         self._nodes: Dict[int, TreeNode] = {}

#     def inorder(self) -> None:
#         def _inorder(node: Optional[TreeNode]) -> None:
#             if node:
#                 _inorder(node.left)
#                 print(f"({node.index}) {node.key}")
#                 _inorder(node.right)

#         if self._root:
#             _inorder(self._root)

#     def populate_tree(self, data: List[Tuple[int, int, Optional[int], Optional[int]]]) -> None:
#         for index, key, left, right in data:
#             if index not in self._nodes:
#                 self._nodes[index] = TreeNode(key, index)
#             node = self._nodes[index]

#             if left is not None:
#                 if left not in self._nodes:
#                     self._nodes[left] = TreeNode(None, left)
#                 node.left = self._nodes[left]
#                 node.left.val = data[left - 1][1]

#             if right is not None:
#                 if right not in self._nodes:
#                     self._nodes[right] = TreeNode(None, right)
#                 node.right = self._nodes[right]
#                 node.right.val = data[right - 1][1]

#         self._root = self._nodes[6]  # Assuming the root is at index 6

#     def draw_tree(self) -> None:
#         pass


# # Data in the format (index, key, left, right)
# data: List[Tuple[int, int, Optional[int], Optional[int]]] = [
#     (1, 17, 8, 9),
#     (2, 14, None, None),
#     (3, 12, None, None),
#     (4, 20, 10, None),
#     (5, 33, 2, None),
#     (6, 15, 1, 4),
#     (7, 28, None, None),
#     (8, 22, None, None),
#     (9, 13, 3, 7),
#     (10, 25, None, 5)
# ]

# # Creating the binary tree
# binary_tree = BinaryTree()

# # Populating the binary tree with data
# binary_tree.populate_tree(data)

# print("Inorder traversal of the binary tree with indices is:")
# binary_tree.inorder()
