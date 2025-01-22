# 2062. Count Vowel Substrings of a String
# https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        length = len(word)
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        return sum(set(word[i:j]) == vowels_set for i in range(length) for j in range(i + 1, length + 1))
