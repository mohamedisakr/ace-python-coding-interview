import pytest
from node import Node
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

# ------ pre order ----- #

# ------ in order ----- #


# @pytest.fixture
# def empty_tree():
#     return BinaryTree(None)


@pytest.fixture
def single_node_tree():
    tree = BinaryTree(1)
    return tree


@pytest.fixture
def left_skewed_tree():
    tree = BinaryTree(3)
    tree.root.left = Node(2)
    tree.root.left.left = Node(1)
    return tree


@pytest.fixture
def right_skewed_tree():
    tree = BinaryTree(1)
    tree.root.right = Node(2)
    tree.root.right.right = Node(3)
    return tree


@pytest.fixture
def balanced_tree():
    tree = BinaryTree(2)
    tree.root.left = Node(1)
    tree.root.right = Node(3)
    return tree


@pytest.fixture
def unbalanced_tree():
    tree = BinaryTree(1)
    tree.root.right = Node(2)
    tree.root.right.right = Node(3)
    tree.root.right.right.right = Node(4)
    return tree


@pytest.fixture
def tree_with_duplicates():
    tree = BinaryTree(2)
    tree.root.left = Node(1)
    tree.root.right = Node(2)
    tree.root.right.right = Node(3)
    return tree


@pytest.fixture
def large_tree():
    tree = BinaryTree(10)
    current = tree.root
    for i in range(9, 0, -1):
        current.left = Node(i)
        current = current.left
    return tree


# def test_empty_tree(empty_tree):
#     # assert empty_tree.in_order_print() == " -"
#     with pytest.raises(TypeError):
#         BinaryTree(None)


def test_single_node_tree(single_node_tree):
    assert single_node_tree.in_order_print() == "1 -"


def test_left_skewed_tree(left_skewed_tree):
    assert left_skewed_tree.in_order_print() == "1 - 2 - 3 -"


def test_right_skewed_tree(right_skewed_tree):
    assert right_skewed_tree.in_order_print() == "1 - 2 - 3 -"


def test_balanced_tree(balanced_tree):
    assert balanced_tree.in_order_print() == "1 - 2 - 3 -"


def test_unbalanced_tree(unbalanced_tree):
    assert unbalanced_tree.in_order_print() == "1 - 2 - 3 - 4 -"


def test_tree_with_duplicates(tree_with_duplicates):
    assert tree_with_duplicates.in_order_print() == "1 - 2 - 2 - 3 -"


def test_large_tree(large_tree):
    expected_output = " - ".join(map(str, range(1, 11))) + " -"
    assert large_tree.in_order_print() == expected_output
