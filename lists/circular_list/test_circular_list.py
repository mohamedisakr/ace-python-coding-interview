import pytest
# Replace 'your_module' with the actual module name
from circular_list import CircularList


@pytest.fixture
def circular_list():
    return CircularList([1, 2, 3, 4, 5])


def test_getitem(circular_list):
    cl = circular_list
    assert cl[0] == 1
    assert cl[1] == 2
    assert cl[len(cl)] == cl[0]
    assert cl[-1] == cl[len(cl) - 1]
    assert cl[len(cl) + 1] == cl[1]
    assert cl[-len(cl) - 1] == cl[len(cl) - 1]
    assert cl[1000000] == cl[1000000 % len(cl)]
    assert cl[-1000000] == cl[-1000000 % len(cl)]


def test_setitem(circular_list):
    cl = circular_list
    cl[0] = 10
    assert cl[0] == 10
    cl[1] = 20
    assert cl[1] == 20
    cl[len(cl)] = 30
    assert cl[0] == 30
    cl[-1] = 40
    assert cl[len(cl) - 1] == 40
    cl[len(cl) + 1] = 50
    assert cl[1] == 50
    cl[-len(cl) - 1] = 60
    assert cl[len(cl) - 1] == 60
    cl[1000000] = 70
    assert cl[1000000 % len(cl)] == 70
    cl[-1000000] = 80
    assert cl[-1000000 % len(cl)] == 80


def test_get_item_with_distance(circular_list):
    cl = circular_list
    assert cl.get_item_with_distance(1, 0) == 1
    assert cl.get_item_with_distance(1, 1) == 2
    assert cl.get_item_with_distance(1, len(cl)) == 1
    assert cl.get_item_with_distance(1, -1) == 5
    assert cl.get_item_with_distance(1, len(cl) + 1) == 2
    assert cl.get_item_with_distance(1, -len(cl) - 1) == 5
    assert cl.get_item_with_distance(1, 1000000) == cl[1000000 % len(cl)]
    assert cl.get_item_with_distance(1, -1000000) == cl[-1000000 % len(cl)]


def test_set_item_with_distance(circular_list):
    cl = circular_list
    initial_index = cl.index(1)

    cl.set_item_with_distance(1, 0, 10)
    assert cl[initial_index] == 10

    initial_index = cl.index(10)
    cl.set_item_with_distance(10, 1, 20)
    assert cl[(initial_index + 1) % len(cl)] == 20

    initial_index = cl.index(10)
    cl.set_item_with_distance(10, len(cl), 30)
    assert cl[initial_index] == 30

    initial_index = cl.index(10)
    cl.set_item_with_distance(10, -1, 40)
    assert cl[(initial_index - 1) % len(cl)] == 40

    initial_index = cl.index(10)
    cl.set_item_with_distance(10, len(cl) + 1, 50)
    assert cl[(initial_index + 1) % len(cl)] == 50

    initial_index = cl.index(10)
    cl.set_item_with_distance(10, -len(cl) - 1, 60)
    assert cl[(initial_index - 1) % len(cl)] == 60

    initial_index = cl.index(10)
    cl.set_item_with_distance(10, 1000000, 70)
    assert cl[(initial_index + 1000000) % len(cl)] == 70

    initial_index = cl.index(10)
    cl.set_item_with_distance(10, -1000000, 80)
    assert cl[(initial_index - 1000000) % len(cl)] == 80


# def test_set_item_with_distance(circular_list):
#     cl = circular_list
#     initial_index = cl.index(1)

#     cl.set_item_with_distance(1, 0, 10)
#     assert cl[initial_index] == 10

#     cl.set_item_with_distance(1, 1, 20)
#     assert cl[(initial_index + 1) % len(cl)] == 20

#     cl.set_item_with_distance(1, len(cl), 30)
#     assert cl[initial_index] == 30

#     cl.set_item_with_distance(1, -1, 40)
#     assert cl[(initial_index - 1) % len(cl)] == 40

#     cl.set_item_with_distance(1, len(cl) + 1, 50)
#     assert cl[(initial_index + 1) % len(cl)] == 50

#     cl.set_item_with_distance(1, -len(cl) - 1, 60)
#     assert cl[(initial_index - 1) % len(cl)] == 60

#     cl.set_item_with_distance(1, 1000000, 70)
#     assert cl[(initial_index + 1000000) % len(cl)] == 70

#     cl.set_item_with_distance(1, -1000000, 80)
#     assert cl[(initial_index - 1000000) % len(cl)] == 80


# def test_set_item_with_distance(circular_list):
#     cl = circular_list
#     initial_index = cl.index(1)
#     cl.set_item_with_distance(1, 0, 10)
#     assert cl[initial_index] == 10

#     cl.set_item_with_distance(1, 1, 20)
#     assert cl[(initial_index + 1) % len(cl)] == 20

#     cl.set_item_with_distance(1, len(cl), 30)
#     assert cl[initial_index] == 30

#     cl.set_item_with_distance(1, -1, 40)
#     assert cl[(initial_index - 1) % len(cl)] == 40

#     cl.set_item_with_distance(1, len(cl) + 1, 50)
#     assert cl[(initial_index + 1) % len(cl)] == 50

#     cl.set_item_with_distance(1, -len(cl) - 1, 60)
#     assert cl[(initial_index - 1) % len(cl)] == 60

#     cl.set_item_with_distance(1, 1000000, 70)
#     assert cl[(initial_index + 1000000) % len(cl)] == 70

#     cl.set_item_with_distance(1, -1000000, 80)
#     assert cl[(initial_index - 1000000) % len(cl)] == 80


# def test_set_item_with_distance(circular_list):
#     cl = circular_list
#     cl.set_item_with_distance(1, 0, 10)
#     assert cl[cl.index(1)] == 10
#     cl.set_item_with_distance(1, 1, 20)
#     assert cl[cl.index(1) + 1] == 20
#     cl.set_item_with_distance(1, len(cl), 30)
#     assert cl[cl.index(1)] == 30
#     cl.set_item_with_distance(1, -1, 40)
#     assert cl[cl.index(1) - 1] == 40
#     cl.set_item_with_distance(1, len(cl) + 1, 50)
#     assert cl[cl.index(1) + 1] == 50
#     cl.set_item_with_distance(1, -len(cl) - 1, 60)
#     assert cl[cl.index(1) - 1] == 60
#     cl.set_item_with_distance(1, 1000000, 70)
#     assert cl[cl.index(1) + 1000000] == 70
#     cl.set_item_with_distance(1, -1000000, 80)
#     assert cl[cl.index(1) - 1000000] == 80


if __name__ == "__main__":
    pytest.main()
