# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        return sum(stone in jewels_set for stone in stones)


sol = Solution()
jewels = "z"
stones = "ZZ"
print(sol.numJewelsInStones(jewels, stones))

# jewels_count = 0

# for stone in stones:
#     if stone in jewels_set:
#         jewels_count += 1
# return jewels_count
