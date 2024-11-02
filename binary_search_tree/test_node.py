import pytest
from typing import Optional, Any, Tuple
from node import Node


# Test cases for Node class

def test_node_initialization():
    node = Node(10)
    assert node.value() == 10
    assert node.left() is None
    assert node.right() is None


def test_node_str():
    left_child = Node(5)
    right_child = Node(15)
    node = Node(10, left_child, right_child)
    assert str(node) == "10 (5 ()())(15 ()())"


def test_set_left_and_right():
    root = Node(10)
    left_child = Node(5)
    right_child = Node(15)
    root.set_left(left_child)
    root.set_right(right_child)
    assert root.left() == left_child
    assert root.right() == right_child


def test_find_min_in_subtree():
    root = Node(10, Node(5, Node(2)), Node(15))
    min_node, _ = root.find_min_in_subtree()
    assert min_node.value() == 2


def test_find_max_in_subtree():
    root = Node(10, Node(5), Node(15, None, Node(20)))
    max_node, _ = root.find_max_in_subtree()
    assert max_node.value() == 20


def test_null_children():
    node = Node(10)
    node.set_left(None)
    node.set_right(None)
    assert node.left() is None
    assert node.right() is None


def test_multiple_levels():
    root = Node(10)
    left_child = Node(5, Node(2), Node(7))
    right_child = Node(15, Node(12), Node(20))
    root.set_left(left_child)
    root.set_right(right_child)
    assert str(root) == "10 (5 (2 ()())(7 ()()))(15 (12 ()())(20 ()()))"


def test_non_integer_values():
    root = Node("root", Node("left"), Node("right"))
    assert root.left().value() == "left"
    assert root.right().value() == "right"
    assert str(root) == 'root (left ()())(right ()())'


def test_reassign_children():
    root = Node(10)
    left_child = Node(5)
    right_child = Node(15)
    root.set_left(left_child)
    root.set_right(right_child)
    new_left_child = Node(3)
    root.set_left(new_left_child)
    assert root.left() == new_left_child
    assert root.right() == right_child


def test_large_tree():
    root = Node(10,
                left=Node(5,
                          left=Node(2,
                                    left=Node(1)
                                    ),
                          right=Node(7,
                                     left=Node(6),
                                     right=Node(8)
                                     )
                          ),
                right=Node(15,
                           left=Node(12,
                                     left=Node(11),
                                     right=Node(13)
                                     ),
                           right=Node(20,
                                      left=Node(18),
                                      right=Node(25)
                                      )
                           )
                )
    min_node, _ = root.find_min_in_subtree()
    max_node, _ = root.find_max_in_subtree()
    assert min_node.value() == 1, f"Expected min value 1, got {min_node.value}"
    assert max_node.value() == 25, f"Expected max value 25, got {
        max_node.value}"
