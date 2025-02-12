# 657. Robot Return to Origin
# https://leetcode.com/problems/robot-return-to-origin/description/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')


sol = Solution()
test_cases = ["UD", "LL"]
for test_case in test_cases:
    print(sol.judgeCircle(test_case))
