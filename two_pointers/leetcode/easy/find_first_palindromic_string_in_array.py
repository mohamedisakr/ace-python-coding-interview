# 2108. Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word: str) -> bool:
            lo, hi = 0, len(word) - 1
            while lo <= hi:
                if word[lo] != word[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        for word in words:
            if isPalindrome(word):
                return word
        return ""

# class Solution:
#     def firstPalindrome(self, words: List[str]) -> str:
#         for word in words:
#             if word == word[::-1]:
#                 return word
#         return ""
