# 2769. Find the Maximum Achievable Number
# https://leetcode.com/problems/find-the-maximum-achievable-number/description

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (2 * t)


sol = Solution()
# num, t = 4, 1
num = 3
t = 2
x = sol.theMaximumAchievableX(num, t)
print(x)
