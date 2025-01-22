# 1688. Count of Matches in Tournament
# https://leetcode.com/problems/count-of-matches-in-tournament/description/
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1

# matches = 0
# teams = n

# while teams > 0:
#     if teams % 2 == 0:
#         matches += teams/2
#         teams //= 2
#     else:
#         matches += (teams-1)//2
#         teams = (teams - 1) // 2 + 1

# return matches


n = 7
sol = Solution()
print(sol.numberOfMatches(n))
