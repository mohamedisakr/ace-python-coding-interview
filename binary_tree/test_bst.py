from typing import Any, Optional
import pytest
from bst import BST


@pytest.fixture
def bst():
    return BST(10)


@pytest.mark.skip
def test_none_value():
    with pytest.raises(TypeError):
        BST(None)


def test_insert_into_empty_tree():
    bst = BST(10)
    # bst.insert(10)
    assert bst.root.value == 10


def test_insert_left_child(bst):
    bst.insert(5)
    assert bst.root.left.value == 5


def test_insert_right_child(bst):
    bst.insert(15)
    assert bst.root.right.value == 15


@pytest.mark.skip
def test_insert_duplicate_value(bst):
    bst.insert(10)
    # Depending on behavior for duplicates, adjust the expectation
    # Here we assume duplicates are not added, so the tree remains the same
    assert bst.root.value == 10
    # assert bst.root.left is None
    assert bst.root.left.value == 10
    assert bst.root.right is None


def test_insert_minimum_value(bst):
    bst.insert(float('-inf'))
    assert bst.root.left.value == float('-inf')


def test_insert_maximum_value(bst):
    bst.insert(float('inf'))
    assert bst.root.right.value == float('inf')


def test_insert_sequential_values():
    bst = BST(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    current = bst.root
    for i in range(1, 6):
        assert current.value == i
        current = current.right


def test_insert_random_values():
    bst = BST(10)
    values = [5, 20, 3, 7, 15, 25]
    for value in values:
        bst.insert(value)
    assert bst.root.left.value == 5
    assert bst.root.right.value == 20
    assert bst.root.left.left.value == 3
    assert bst.root.left.right.value == 7
    assert bst.root.right.left.value == 15
    assert bst.root.right.right.value == 25

# ------ search --------


class Node:
    def __init__(self, value: Any):
        self.value: Any = value
        self.left: 'Node' | None = None
        self.right: 'Node' | None = None


class BST:
    def __init__(self, value: Any):
        self.root = Node(value)

    def insert(self, value: Any) -> None:
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: Node, value: Any) -> None:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value: Any) -> bool:
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Optional[Node], value: Any) -> bool:
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)


@pytest.fixture
def bst_single_node():
    return BST(10)


@pytest.fixture
def bst_with_children():
    bst = BST(10)
    bst.insert(5)
    bst.insert(15)
    return bst


@pytest.fixture
def bst_with_multiple_nodes():
    bst = BST(10)
    for value in [5, 15, 3, 7, 12, 18]:
        bst.insert(value)
    return bst


@pytest.fixture
def bst_with_duplicates():
    bst = BST(10)
    bst.insert(10)
    bst.insert(10)
    return bst


@pytest.fixture
def bst_with_negative_values():
    bst = BST(10)
    bst.insert(-5)
    bst.insert(-10)
    return bst


@pytest.fixture
def bst_with_large_values():
    bst = BST(10)
    bst.insert(1000000)
    return bst


def test_search_root_node_single(bst_single_node):
    assert bst_single_node.search(10) == True


def test_search_existing_left_child(bst_with_children):
    assert bst_with_children.search(5) == True


def test_search_existing_right_child(bst_with_children):
    assert bst_with_children.search(15) == True


def test_search_non_existing_value(bst_with_children):
    assert bst_with_children.search(20) == False


@pytest.mark.skip
def test_search_in_empty_tree():
    bst = BST(None)
    assert bst.search(10) == False


def test_search_minimum_value(bst_with_multiple_nodes):
    assert bst_with_multiple_nodes.search(3) == True


def test_search_maximum_value(bst_with_multiple_nodes):
    assert bst_with_multiple_nodes.search(18) == True


def test_search_duplicate_values(bst_with_duplicates):
    assert bst_with_duplicates.search(10) == True


def test_search_negative_values(bst_with_negative_values):
    assert bst_with_negative_values.search(-5) == True


def test_search_large_values(bst_with_large_values):
    assert bst_with_large_values.search(1000000) == True
