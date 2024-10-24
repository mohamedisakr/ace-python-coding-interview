import pytest
from binarytree import BinaryTree


def test_single_node_initialization():
    tree = BinaryTree(10)
    assert tree.root.value == 10
    assert tree.root.left is None
    assert tree.root.right is None


@pytest.mark.parametrize("value", [0, -1])
def test_unusual_valid_values(value):
    tree = BinaryTree(value)
    assert tree.root.value == value
    assert tree.root.left is None
    assert tree.root.right is None


def test_large_value():
    tree = BinaryTree(1000000)
    assert tree.root.value == 1000000
    assert tree.root.left is None
    assert tree.root.right is None


def test_floating_point_value():
    tree = BinaryTree(3.14)
    assert tree.root.value == 3.14
    assert tree.root.left is None
    assert tree.root.right is None


def test_string_value():
    tree = BinaryTree("root")
    assert tree.root.value == "root"
    assert tree.root.left is None
    assert tree.root.right is None


def test_none_value():
    with pytest.raises(TypeError):
        BinaryTree(None)
