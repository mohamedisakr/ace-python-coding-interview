import pytest
from node import Node


def test_node_initialization():
    node = Node(10)
    assert str(node) == "10 ()()"


def test_node_with_children():
    node = Node(10, Node(5), Node(15))
    assert str(node) == "10 (5 ()())(15 ()())"


def test_value_accessor():
    node = Node(10)
    assert node.value == 10


def test_left_right_accessors():
    node = Node(10, Node(5))
    assert str(node.left) == "5 ()()"
    assert node.right is None


# def test_left_right_mutators():
#     node = Node(10)
#     node.left = Node(5)
#     node.right = Node(15)
#     assert
