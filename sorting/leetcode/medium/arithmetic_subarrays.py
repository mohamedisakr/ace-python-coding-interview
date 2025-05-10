from typing import List


class Solution:
    def is_arithmetic(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        common_diff = nums[1] - nums[0]
        for i in range(1, n - 1):
            if common_diff != nums[i + 1] - nums[i]:
                return False
        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        ans = []

        for i in range(m):
            sub_arr = nums[l[i]:r[i]+1]
            ans.append(self.is_arithmetic(sub_arr))
        return ans


nums = [4, 6, 5, 9, 3, 7]
l = [0, 0, 2]
r = [2, 3, 5]
sol = Solution()
print(sol.checkArithmeticSubarrays(nums, l, r))

# [4,6,5]
# [4,6,5,9]
# [5,9,3,7]

# arr = [3, 5, 7, 9]
# arr.sort(reverse=True)
# print(arr)

# gemini


def is_arithmetic_optimized(nums: List[int]) -> bool:
    n = len(nums)
    if n <= 2:
        return True

    min_val = min(nums)
    max_val = max(nums)

    if (max_val - min_val) % (n - 1) != 0:
        return False

    diff = (max_val - min_val) // (n - 1)

    seen = set()
    for num in nums:
        if (num - min_val) % diff != 0:
            return False
        expected_index = (num - min_val) // diff
        if expected_index >= n or num in seen:
            return False
        seen.add(num)

    return len(seen) == n
