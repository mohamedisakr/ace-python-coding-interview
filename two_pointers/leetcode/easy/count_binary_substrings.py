# 696. Count Binary Substrings
# https://leetcode.com/problems/count-binary-substrings/description/

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        prev, curr = 0, 1

        for i in range(1, n):
            if s[i] != s[i-1]:
                count += min(curr, prev)
                prev = curr
                curr = 1
            else:
                curr += 1
        return count + min(curr, prev)
