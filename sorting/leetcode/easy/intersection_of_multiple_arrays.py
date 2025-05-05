from collections import Counter
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        counter = Counter()

        for arr in nums:
            counter.update(set(arr))

        intersec = [num for num in counter if counter[num] == n]
        return sorted(intersec)


nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
my_sol = Solution()
print(my_sol.intersection(nums))


# array = [
#     [1, 2, 3],
#     [4, 5],
#     [6, 7, 8, 9]
# ]

# # Number of rows
# num_rows = len(array)

# # Maximum number of columns
# num_cols = max(len(row) for row in array)

# print(f"Number of rows: {num_rows}")
# print(f"Maximum number of columns: {num_cols}")
