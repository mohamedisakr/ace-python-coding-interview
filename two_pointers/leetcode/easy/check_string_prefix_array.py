# 1961. Check If String Is a Prefix of Array
# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/description/

from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = []
        for word in words:
            prefix.append(word)
            if ''.join(prefix) == s:
                return True
        return False

# return "".join(words).startswith(s)
