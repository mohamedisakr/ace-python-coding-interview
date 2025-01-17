# 2114. Maximum Number of Words Found in Sentences
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for sentence in sentences:
            words = sentence.split()
            max_words = max(max_words, len(words))

        return max_words


sol = Solution()
sentences = ["alice and bob love leetcode",
             "i think so too", "this is great thanks very much"]
max_words = sol.mostWordsFound(sentences)
print(max_words)
