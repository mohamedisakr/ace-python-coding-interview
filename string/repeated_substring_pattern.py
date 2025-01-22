# 459. Repeated Substring Pattern
# https://leetcode.com/problems/repeated-substring-pattern/description/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s+s).index(s, 1) < len(s)
