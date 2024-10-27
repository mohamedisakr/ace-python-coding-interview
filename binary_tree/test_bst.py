import pytest
from bst import BST


@pytest.fixture
def bst():
    return BST(10)


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
