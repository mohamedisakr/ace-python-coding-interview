# 682. Baseball Game
# https://leetcode.com/problems/baseball-game/description/

from typing import List

# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for operation in operations:
            match operation:
                case '+':
                    scores.append(scores[-1] + scores[-2])
                case 'D':
                    scores.append(scores[-1] * 2)
                case 'C':
                    scores.pop()
                case _:
                    scores.append(int(operation))

        return sum(scores)
