from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even_nums = [nums[i] for i in range(n) if i % 2 == 0]
        odd_nums = [nums[i] for i in range(n) if i % 2 != 0]

        odd_nums.sort(reverse=True)
        even_nums.sort()

        formed = [0] * n
        even_index, odd_index = 0, 0

        for i in range(n):
            if i % 2 == 0:
                formed[i] = even_nums[even_index]
                even_index += 1
            else:
                formed[i] = odd_nums[odd_index]
                odd_index += 1

        return formed
