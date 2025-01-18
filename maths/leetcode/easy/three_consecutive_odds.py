# 1550. Three Consecutive Odds
# https://leetcode.com/problems/three-consecutive-odds/description/

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = 0
        for num in arr:
            if num % 2 == 1:
                odds += 1
            else:
                odds = 0  # reset counter

            if odds == 3:
                return True
        return False

        # n = len(arr)
        # for i in range(2, n, 1):
        #     if arr[i-2] % 2 != 0 and arr[i-1] % 2 != 0 and arr[i] % 2 != 0:
        #         return True
        # return False


sol = Solution()
arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
print(sol.threeConsecutiveOdds(arr))
