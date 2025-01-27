# 1160. Find Words That Can Be Formed by Characters
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description
from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = Counter(chars)
        total = 0

        for word in words:
            word_counter = Counter(word)
            if all(word_counter[ch] <= chars_counter[ch] for ch in word_counter):
                total += len(word)
        return total


sol = Solution()
# words, chars = ["cat", "bt", "hat", "tree"], "atach"
words, chars = ["hello", "world", "leetcode"], "welldonehoneyr"
print(sol.countCharacters(words, chars))

# class Solution:
#     def countCharacters(self, words: List[str], chars: str) -> int:
#         total_lengths = 0
#         for word in words:
#             word_len = 0
#             for ch in word:
#                 if ch not in chars:
#                     word_len = 0
#                     break
#                 word_len += 1
#             total_lengths += word_len
#         return total_lengths
