from typing import List


class Solution:

    def calculate(self, nums: List[int]) -> int:
        # Initialize a new array prefixSum of the same size as the input array.
        # Set the first element of prefixSum to be the same as the first element of arr.
        # For each subsequent element, add the current element of arr to the previous element of prefixSum.
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]

        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1] + nums[i]

        return prefix_sum


nums = [4, 5, 2, 1]
sol = Solution()
print(sol.calculate(nums))
