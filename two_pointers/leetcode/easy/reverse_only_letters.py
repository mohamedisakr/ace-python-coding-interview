# 917. Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/description/

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = list(s)
        n = len(s) - 1
        lo, hi = 0, n
        while lo < hi:
            while lo < hi and not letters[lo].isalpha():
                lo += 1
            while lo < hi and not letters[hi].isalpha():
                hi -= 1
            letters[lo], letters[hi] = letters[hi], letters[lo]
            lo += 1
            hi -= 1
        return ''.join(letters)
