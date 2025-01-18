# 2942. Find Words Containing Character
# https://leetcode.com/problems/find-words-containing-character/description
from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]

# indices = []
# for i, w in enumerate(words):
#     if x in words[i]:
#         indices.append(i)
# return indices
