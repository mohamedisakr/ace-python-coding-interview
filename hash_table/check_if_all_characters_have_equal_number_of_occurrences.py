# 1941. Check if All Characters Have Equal Number of Occurrences
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

from typing import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        occurrences = set(counter.values())
        return len(occurrences) == 1


# return len(set(Counter(s).values())) == 1


s = "abacbc"
sol = Solution()
sol.areOccurrencesEqual(s)

# def areOccurrencesEqual(self, s: str) -> bool:
#     counter = Counter(s)
#     n = len(counter)
#     for i in range(1, n, 1):
#         if counter[i - 1] != counter[i]:
#             return False
#     return True
