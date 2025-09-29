# https://leetcode.com/problems/bitwise-or-of-adjacent-elements/description/
# from itertools import pairwise
from typing import List


def orArray(nums: List[int]) -> List[int]:
    # return [a | b for a, b in pairwise(nums)]
    n = len(nums)
    answer = []
    for i in range(1, n):
        answer.append(nums[i - 1] | nums[i])
    return answer


nums = [5, 4, 9, 11]  # [8, 4, 2]  # [1, 3, 7, 15]
print(orArray(nums))
