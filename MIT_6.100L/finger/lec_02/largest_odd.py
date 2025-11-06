from typing import List


def largest_odd(nums: List[int]) -> int | None:
    if not isinstance(nums, list) or len(nums) != 10:
        raise ValueError("Input must be a list of exactly 10 integers.")

    if not all(isinstance(n, int) for n in nums):
        raise TypeError("All elements must be integers.")

    max_odd = None
    for num in nums:
        if num % 2 != 0:
            if max_odd is None or num > max_odd:
                max_odd = num
    return max_odd


# from typing import List


# def largest_odd(nums: List[int]) -> int:
#     max_odd = nums[0]
#     for num in nums:
#         if num % 2 != 0 and num > max_odd:
#             max_odd = num
#     return max_odd
