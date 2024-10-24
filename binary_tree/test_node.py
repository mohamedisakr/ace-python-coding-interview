import pytest

from node import Node


def test_single_node_initialization():
    node = Node(5)
    assert node.value == 5
    assert node.left is None
    assert node.right is None


@pytest.mark.parametrize("value", [0, -1])
def test_unusual_valid_values(value):
    node = Node(value)
    assert node.value == value
    assert node.left is None
    assert node.right is None


def test_large_value():
    node = Node(1000000)
    assert node.value == 1000000
    assert node.left is None
    assert node.right is None


def test_floating_point_value():
    node = Node(3.14)
    assert node.value == 3.14
    assert node.left is None
    assert node.right is None


def test_string_value():
    node = Node("test")
    assert node.value == "test"
    assert node.left is None
    assert node.right is None

# other test cases


def test_tree_with_multiple_levels():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    assert root.left.value == 2
    assert root.right.value == 3
    assert root.left.left.value == 4
    assert root.left.right.value == 5


class CustomClass:
    pass


def test_custom_objects_as_values():
    custom_obj = CustomClass()
    node = Node(custom_obj)
    assert node.value == custom_obj
    assert node.left is None
    assert node.right is None


def test_nodes_with_only_one_child():
    node = Node(1)
    node.left = Node(2)
    assert node.left.value == 2
    assert node.right is None

    node = Node(1)
    node.right = Node(3)
    assert node.right.value == 3
    assert node.left is None

# Stress test with a large number of nodes could be implemented but is generally
# dependent on specific application needs
