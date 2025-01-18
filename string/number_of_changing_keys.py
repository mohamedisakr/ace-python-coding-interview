# 3019. Number of Changing Keys
# https://leetcode.com/problems/number-of-changing-keys/description/


from itertools import pairwise


class Solution:
    def countKeyChanges(self, s: str) -> int:
        return sum(a.lower() != b.lower() for a, b in pairwise(s))


# changes = 0
# n = len(s) - 1
# for i in range(n):
#     if s[i].lower() != s[i + 1].lower():
#         changes += 1
# return changes
