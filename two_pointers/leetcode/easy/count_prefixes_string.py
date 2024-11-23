# 2255. Count Prefixes of a Given String
# https://leetcode.com/problems/count-prefixes-of-a-given-string/description/
from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(s.startswith(word) for word in words)
