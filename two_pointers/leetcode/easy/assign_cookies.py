# 455. Assign Cookies
# https://leetcode.com/problems/assign-cookies/description/
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m, n = len(g), len(s)
        i, j = 0, 0  # greed factors, cookie sizes
        content = 0

        while i < m and j < n:
            if s[j] >= g[i]:
                content += 1
                i += 1
                j += 1
            else:
                j += 1

        return content
