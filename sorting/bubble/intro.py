from typing import List


def sort(nums: List[int]):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break
    return nums


# nums = [5, 1, 4, 2, 8]
# print(sort(nums))
