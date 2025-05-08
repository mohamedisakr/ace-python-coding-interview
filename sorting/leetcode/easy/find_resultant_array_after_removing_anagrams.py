from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        final_arr = []
        for i, word in enumerate(words):
            if i == 0 or sorted(words[i]) != sorted(words[i - 1]):
                final_arr.append(word)
        return final_arr
