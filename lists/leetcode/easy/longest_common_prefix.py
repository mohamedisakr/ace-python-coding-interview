# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while s.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


# Example usage:
solution = Solution()
# Output: "fl"
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
# Output: ""
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
