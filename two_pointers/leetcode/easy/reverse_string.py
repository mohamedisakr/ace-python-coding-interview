# 344. Reverse String
# https://leetcode.com/problems/reverse-string/description/

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lo, hi = 0, len(s) - 1

        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1


sol = Solution()

arr1 = ["h", "e", "l", "l", "o"]
print(sol.reverseString(arr1))

arr2 = ["H", "a", "n", "n", "a", "h"]
print(sol.reverseString(arr2))
