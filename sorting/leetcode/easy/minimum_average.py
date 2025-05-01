from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        min_avg = float('inf')  # 1.8e308 #
        nums.sort()
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            avg = (nums[lo] + nums[hi]) / 2
            min_avg = min(min_avg, avg)
            lo += 1
            hi -= 1

        return min_avg


# nums = [7, 8, 3, 4, 15, 13, 4, 1]
nums = [1, 2, 3, 7, 8, 9]
sol = Solution()
min_avg = sol.minimumAverage(nums)
print(min_avg)
