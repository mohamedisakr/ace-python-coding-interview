from typing import List


class Solution:
    def countGreaterOrEqual(self, nums: List[int], target: int) -> int:
        """ Binary search to find first index where nums[i] >= target """
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        lo, hi = 0, n

        while lo <= hi:
            mid = (lo + hi) // 2
            count = n - self.countGreaterOrEqual(nums, mid)

            if count == mid:
                return mid
            elif count > mid:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1
