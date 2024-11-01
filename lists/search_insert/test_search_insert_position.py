import pytest
from search_insert_position import Solution


@pytest.mark.parametrize("input_value, expected_output", [
    ([4, 3, 2, 1], [4, 3, 2, 2]),  # first example
    ([4, 3, 2, 1], [4, 3, 2, 2]),  # second example
    ([4, 3, 2, 1], [4, 3, 2, 2]),  # third example
])
def test_plusOne(input_value, expected_output):
    sol = Solution()
    assert sol.searchInsert(input_value) == expected_output
