# 2825. Make String a Subsequence Using Cyclic Increments
# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        n = len(str2)

        for char in str1:
            next_char = 'a' if char == 'z' else chr(ord(char)+1)
            if i < n:
                if str2[i] in (char, next_char):
                    i += 1

        return i == n
