# 1528. Shuffle String
# https://leetcode.com/problems/shuffle-string/description/

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        shuffled = ['']*n
        for i, c in enumerate(s):
            shuffled[indices[i]] = c
        return "".join(shuffled)


sol = Solution()
s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
print(sol.restoreString(s, indices))
