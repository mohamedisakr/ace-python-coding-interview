# 2351. First Letter to Appear Twice
# https://leetcode.com/problems/first-letter-to-appear-twice/description/

from collections import Counter

# Input: s = "abccbaacz"
# Output: "c"


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        counter = Counter()
        for ch in s:
            if ch in counter:
                return ch
            counter[ch] += 1


sol = Solution()
s = "abccbaacz"
print(sol.repeatedCharacter(s))
