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


@pytest.fixture
def tree_with_only_left_children():
    tree = BinaryTree(5)
    current = tree.root
    for i in range(4, 0, -1):
        current.left = Node(i)
        current = current.left
    return tree


@pytest.fixture
def tree_with_only_right_children():
    tree = BinaryTree(1)
    current = tree.root
    for i in range(2, 6):
        current.right = Node(i)
        current = current.right
    return tree


@pytest.fixture
def tree_with_mixed_children():
    tree = BinaryTree(4)
    tree.root.left = Node(2)
    tree.root.right = Node(6)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(3)
    tree.root.right.left = Node(5)
    tree.root.right.right = Node(7)
    return tree


@pytest.fixture
def tree_with_null_nodes():
    tree = BinaryTree(4)
    tree.root.left = Node(2)
    tree.root.right = Node(6)
    tree.root.left.right = Node(3)
    tree.root.right.left = Node(5)
    return tree


@pytest.fixture
def tree_with_negative_values():
    tree = BinaryTree(-1)
    tree.root.left = Node(-2)
    tree.root.right = Node(0)
    tree.root.left.left = Node(-3)
    tree.root.left.right = Node(-1.5)
    return tree


@pytest.fixture
def tree_with_non_integer_values():
    tree = BinaryTree("root")
    tree.root.left = Node("left")
    tree.root.right = Node("right")
    tree.root.left.left = Node("left.left")
    tree.root.left.right = Node("left.right")
    return tree


def test_tree_with_only_left_children(tree_with_only_left_children):
    assert tree_with_only_left_children.in_order_print() == "1 - 2 - 3 - 4 - 5 -"


def test_tree_with_only_right_children(tree_with_only_right_children):
    assert tree_with_only_right_children.in_order_print() == "1 - 2 - 3 - 4 - 5 -"


def test_tree_with_mixed_children(tree_with_mixed_children):
    assert tree_with_mixed_children.in_order_print() == "1 - 2 - 3 - 4 - 5 - 6 - 7 -"


def test_tree_with_null_nodes(tree_with_null_nodes):
    assert tree_with_null_nodes.in_order_print() == "2 - 3 - 4 - 5 - 6 -"


def test_tree_with_negative_values(tree_with_negative_values):
    assert tree_with_negative_values.in_order_print() == "-3 - -2 - -1.5 - -1 - 0 -"


def test_tree_with_non_integer_values(tree_with_non_integer_values):
    assert tree_with_non_integer_values.in_order_print(
    ) == "left.left - left - left.right - root - right -"

# ------- post order --------


def test_single_node():
    tree = BinaryTree(1)
    assert tree.post_order_print() == '1 -'


def test_two_level_tree():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    assert tree.post_order_print() == '2 - 3 - 1 -'


def test_empty_tree():
    # Modify this if the BinaryTree should support an empty initialization
    tree = BinaryTree(1)
    tree.root = None
    assert tree.post_order_print() == ' -'

# -------- level order --------


def test_single_node_level():
    tree = BinaryTree(1)
    assert tree.level_order_print() == '1 -'


def test_two_level_tree_level():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    assert tree.level_order_print() == '1 - 2 - 3 -'


def test_unbalanced_tree_level():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.left.left = Node(3)
    assert tree.level_order_print() == '1 - 2 - 3 -'


def test_empty_tree_level():
    # Modify this if the BinaryTree should support an empty initialization
    tree = BinaryTree(1)
    tree.root = None
    assert tree.level_order_print() == ''


def test_tree_with_only_left_children_level():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.left.left = Node(3)
    assert tree.level_order_print() == '1 - 2 - 3 -'


def test_tree_with_only_right_children_level():
    tree = BinaryTree(1)
    tree.root.right = Node(2)
    tree.root.right.right = Node(3)
    assert tree.level_order_print() == '1 - 2 - 3 -'


@pytest.mark.skip
def test_large_tree_level():
    tree = BinaryTree(1)
    # Create a large tree by adding nodes
    for i in range(2, 21):
        tree.root.right = Node(i)
    # Expected output would be '1 - 2 - 3 - ... - 20 -'
    expected_output = ' - '.join(map(str, range(1, 21))) + ' -'
    assert tree.level_order_print() == expected_output

# ----- reverse level order ---------


@pytest.fixture
def tree_single_node():
    return BinaryTree(1)


@pytest.fixture
def tree_two_level():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    return tree


@pytest.fixture
def tree_unbalanced():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.left.left = Node(3)
    return tree


@pytest.fixture
def tree_with_only_left_children_reverse():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.left.left = Node(3)
    return tree


@pytest.fixture
def tree_with_only_right_children_reverse():
    tree = BinaryTree(1)
    tree.root.right = Node(2)
    tree.root.right.right = Node(3)
    return tree


@pytest.fixture
def tree_large():
    tree = BinaryTree(1)
    # Create a large tree by adding nodes
    current = tree.root
    for i in range(2, 21):
        node = Node(i)
        current.right = node
        current = node
    return tree


def test_single_node_reverse(tree_single_node):
    assert tree_single_node.reverse_level_order_print() == '1-'

# def test_two_level_tree(tree_two_level):
#     assert tree_two_level

# ------ grouping level order --------

# @pytest.fixture
# def tree_single_node():
#     return BinaryTree(1)


# @pytest.fixture
# def tree_two_level():
#     tree = BinaryTree(1)
#     tree.root.left = Node(2)
#     tree.root.right = Node(3)
#     return tree


# @pytest.fixture
# def tree_unbalanced():
#     tree = BinaryTree(1)
#     tree.root.left = Node(2)
#     tree.root.left.left = Node(3)
#     return tree


# @pytest.fixture
# def tree_with_only_left_children():
#     tree = BinaryTree(1)
#     tree.root.left = Node(2)
#     tree.root.left.left = Node(3)
#     return tree


# @pytest.fixture
# def tree_with_only_right_children():
#     tree = BinaryTree(1)
#     tree.root.right = Node(2)
#     tree.root.right.right = Node(3)
#     return tree


# @pytest.fixture
# def tree_large():
#     tree = BinaryTree(1)
#     # Create a large tree by adding nodes
#     for i in range(2, 21):
#         current = tree.root
#         while current.right is not None:
#             current = current.right
#         current.right = Node(i)
#     return tree


# def test_single_node(tree_single_node):
#     assert tree_single_node.level_order_print() == '1 - '


# def test_two_level_tree(tree_two_level):
#     assert tree_two_level.level_order_print() == '1 - 2 - 3 - '


# def test_unbalanced_tree(tree_unbalanced):
#     assert tree_unbalanced.level_order_print() == '1 - 2 - 3 - '


# def test_with_only_left_children(tree_with_only_left_children):
#     assert tree_with_only_left_children.level_order_print() == '1 - 2 - 3 - '


# def test_with_only_right_children(tree_with_only_right_children):
#     assert tree_with_only_right_children.level_order_print() == '1 - 2 - 3 - '


# def test_large_tree(tree_large):
#     expected_output = ' - '.join(map(str, range(1, 21))) + ' -'
#     assert tree_large.level_order_print() == expected_output
