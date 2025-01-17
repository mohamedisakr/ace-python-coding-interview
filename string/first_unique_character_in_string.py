# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/description

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, v in enumerate(s):
            if counter[v] == 1:
                return i

        return -1


# if "__name__" == "__main__":
sol = Solution()
s = "aabb"
idx = sol.firstUniqChar(s)
print(idx)
