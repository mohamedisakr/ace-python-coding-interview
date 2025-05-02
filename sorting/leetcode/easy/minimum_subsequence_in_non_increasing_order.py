from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        subsequence = []
        running_total = 0
        nums.sort(reverse=True)

        for num in nums:
            running_total += num
            subsequence.append(num)

            if running_total > total_sum - running_total:
                break

        return subsequence
