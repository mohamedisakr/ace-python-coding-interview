# 942. DI String Match
# https://leetcode.com/problems/di-string-match/description/

from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        perm = []
        lo, hi = 0, len(s)

        for char in s:
            if char == 'I':
                perm.append(lo)
                lo += 1
            else:
                perm.append(hi)
                hi -= 1

        perm.append(lo)

        return perm
