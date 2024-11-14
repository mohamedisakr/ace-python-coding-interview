# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        i, j = 0, 0

        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1

        return True if i == m else False
