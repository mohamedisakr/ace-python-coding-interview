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

# ---- other test cases -------


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


def test_boolean_value():
    tree_true = BinaryTree(True)
    assert tree_true.root.value == True
    assert tree_true.root.left is None
    assert tree_true.root.right is None

    tree_false = BinaryTree(False)
    assert tree_false.root.value == False
    assert tree_false.root.left is None
    assert tree_false.root.right is None


def test_min_max_integers():
    tree_min = BinaryTree(-2**31)
    assert tree_min.root.value == -2**31
    assert tree_min.root.left is None
    assert tree_min.root.right is None

    tree_max = BinaryTree(2**31 - 1)
    assert tree_max.root.value == 2**31 - 1
    assert tree_max.root.left is None
    assert tree_max.root.right is None


def test_empty_string():
    tree = BinaryTree("")
    assert tree.root.value == ""
    assert tree.root.left is None
    assert tree.root.right is None


def test_whitespace_string():
    tree = BinaryTree("   ")
    assert tree.root.value == "   "
    assert tree.root.left is None
    assert tree.root.right is None
