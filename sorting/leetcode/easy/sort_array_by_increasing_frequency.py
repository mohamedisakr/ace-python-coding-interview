from typing import Counter, List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        nums.sort(key=lambda n: (counter[n], -n))
        return nums
