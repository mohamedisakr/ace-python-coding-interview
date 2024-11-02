import pytest
from typing import Tuple, Optional, Any
from node import Node
from bst import BinarySearchTree


class TestBinarySearchTree:
    @pytest.fixture
    def bst(self) -> BinarySearchTree:
        bst = BinarySearchTree(10)
        bst._root._left = Node(5, Node(2), Node(7))
        bst._root._right = Node(15, Node(12), Node(17))
        return bst

    def test_search_target_is_root(self, bst: BinarySearchTree):
        node, parent = bst._search(10)
        assert node is not None and node.value == 10
        assert parent is None

    def test_search_target_in_left_subtree(self, bst: BinarySearchTree):
        node, parent = bst._search(5)
        assert node is not None and node.value == 5
        assert parent is not None and parent.value == 10

    def test_search_target_in_right_subtree(self, bst: BinarySearchTree):
        node, parent = bst._search(15)
        assert node is not None and node.value == 15
        assert parent is not None and parent.value == 10

    def test_search_target_less_than_all_elements(self, bst: BinarySearchTree):
        node, parent = bst._search(1)
        assert node is None
        assert parent is None

    def test_search_target_greater_than_all_elements(self, bst: BinarySearchTree):
        node, parent = bst._search(20)
        assert node is None
        assert parent is None

    def test_search_target_is_leaf(self, bst: BinarySearchTree):
        node, parent = bst._search(2)
        assert node is not None and node.value == 2
        assert parent is not None and parent.value == 5

    def test_search_empty_tree(self):
        bst = BinarySearchTree(10)
        bst._root = None
        node, parent = bst._search(10)
        assert node is None
        assert parent is None

    def test_search_single_element_tree(self):
        bst = BinarySearchTree(10)
        node, parent = bst._search(10)
        assert node is not None and node.value == 10
        assert parent is None

    def test_search_tree_with_only_left_children(self):
        bst = BinarySearchTree(10)
        bst._root._left = Node(5, Node(3))
        node, parent = bst._search(3)
        assert node is not None and node.value == 3
        assert parent is not None and parent.value == 5

    @pytest.mark.skip('not completed')
    def test_search_tree_with_only_right_children(self):
        bst = BinarySearchTree(10)
        bst

# Test cases for insert function


def test_insert_into_empty_tree():
    bst = BinarySearchTree(10)
    bst.insert(5)
    assert bst._root.left is not None
    assert bst._root.left.value == 5


def test_insert_into_tree_with_existing_nodes():
    bst = BinarySearchTree(10)
    bst.insert(5)
    bst.insert(15)
    assert bst._root.left is not None
    assert bst._root.left.value == 5
    assert bst._root.right is not None
    assert bst._root.right.value == 15


def test_insert_duplicate_values():
    bst = BinarySearchTree(10)
    bst.insert(10)
    assert bst._root.left is not None
    assert bst._root.left.value == 10


def test_insert_leftmost_value():
    bst = BinarySearchTree(10)
    bst.insert(5)
    bst.insert(2)
    assert bst._root.left.left is not None
    assert bst._root.left.left.value == 2


def test_insert_rightmost_value():
    bst = BinarySearchTree(10)
    bst.insert(15)
    bst.insert(20)
    assert bst._root.right.right is not None
    assert bst._root.right.right.value == 20


def test_insert_single_node_tree():
    bst = BinarySearchTree(10)
    bst.insert(5)
    bst.insert(15)
    assert bst._root._left is not None
    assert bst._root._left.value == 5
    assert bst._root._right is not None
    assert bst._root._right.value == 15
