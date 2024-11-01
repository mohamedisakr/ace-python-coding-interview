import pytest
from search_insert_position import Solution


@pytest.mark.parametrize("nums, target, expected", [
    ([1, 3, 5, 6], 5, 2),  # Target Present in the List
    ([1, 3, 5, 6], 2, 1),  # Target Not Present, Insert in the Middle
    ([1, 3, 5, 6], 0, 0),  # Target Less Than All Elements
    ([1, 3, 5, 6], 7, 4),  # Target Greater Than All Elements
    ([1, 3, 5, 6], 1, 0),  # Target as First Element
    ([1, 3, 5, 6], 6, 3),  # Target as Last Element
    ([], 1, 0),  # Empty List
    ([5], 2, 0),  # Single Element List, Target Less
    ([5], 7, 1),  # Single Element List, Target Greater
    ([2, 2, 2, 2], 3, 4),  # Multiple Elements, All Same, Target Different
    ([1, 3, 5, 6], 5,  2),  # first example
    ([1, 3, 5, 6], 2,  1),  # second example
    ([1, 3, 5, 6], 7,  4)  # third example
])
def test_searchInsert(nums, target, expected):
    sol = Solution()
    assert sol.searchInsert(nums, target) == expected
