from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Store (value, index) pairs
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        # Step 2: Sort by value in descending order
        indexed_nums.sort(key=lambda x: x[0], reverse=True)
        # Step 3: Select the first K elements and their indices
        selected = sorted(indexed_nums[:k], key=lambda x: x[1])
        # Step 4: Extract values in original order
        return [num for num, _ in selected]


nums = [3, 1, 5, 7, 9]
k = 3
my_sol = Solution()
print(my_sol.maxSubsequence(nums, k))
# nums = [2, 1, 3, 3]
# k = 2
# nums = [-1, -2, 3, 4]
# k = 3
