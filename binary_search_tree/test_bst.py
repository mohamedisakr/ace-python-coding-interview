import pytest
from typing import Tuple, Optional, Any
from node import Node
from bst import BinarySearchTree


def test_bst_initialization():
    bst = BinarySearchTree()
    assert bst._root is None


def test_bst_insert_into_empty_tree():
    bst = BinarySearchTree()
    bst.insert(10)
    assert bst._root is not None
    assert bst._root.value() == 10


def test_bst_insert_into_tree_with_existing_nodes():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    assert bst._root.left() is not None
    assert bst._root.left().value() == 5
    assert bst._root.right() is not None
    assert bst._root.right().value() == 15


def test_bst_insert_duplicate_values():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(10)
    assert bst._root.left() is not None
    assert bst._root.left().value() == 10


def test_bst_insert_leftmost_value():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(2)
    assert bst._root.left().left() is not None
    assert bst._root.left().left().value() == 2


def test_bst_insert_rightmost_value():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(15)
    bst.insert(20)
    assert bst._root.right().right() is not None
    assert bst._root.right().right().value() == 20


def test_bst_contains_existing_value():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    assert bst.contains(5) == True
    assert bst.contains(15) == True


def test_bst_contains_non_existing_value():
    bst = BinarySearchTree()
    bst.insert(10)
    assert bst.contains(20) == False


def test_bst_search_existing_value():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    node, parent = bst._search(5)
    assert node is not None
    assert node.value() == 5
    assert parent.value() == 10


def test_bst_search_non_existing_value():
    bst = BinarySearchTree()
    bst.insert(10)
    node, parent = bst._search(20)
    assert node is None
    assert parent is None


def test_bst_search_root_value():
    bst = BinarySearchTree()
    bst.insert(10)
    node, parent = bst._search(10)
    assert node is not None
    assert node.value() == 10
    assert parent is None


def test_bst_str_repr():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    assert str(bst) == '10 (5 ()())(15 ()())'
    assert repr(bst) == 'BinarySearchTree(10 (5 ()())(15 ()()))'


# Test cases for delete function


def test_delete_from_empty_tree():
    bst = BinarySearchTree()
    with pytest.raises(ValueError, match="Delete on an empty tree"):
        bst.delete(10)


def test_delete_non_existent_value():
    bst = BinarySearchTree()
    bst.insert(10)
    with pytest.raises(ValueError, match="Value not found"):
        bst.delete(20)


def test_delete_leaf_node():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.delete(5)
    assert bst._root.left() is None


def test_delete_node_with_one_child():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.delete(5)
    assert bst._root.left().value() == 2


def test_delete_node_with_two_children():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(7)
    bst.delete(5)
    assert bst._root.left().value() == 2
    assert bst._root.left().right().value() == 7


def test_delete_root_node():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.delete(10)
    assert bst._root.value() in [5, 15]  # New root should be either 5 or 15


def test_delete_duplicate_values():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(10)
    bst.delete(10)
    assert bst._root.left() is None  # not
