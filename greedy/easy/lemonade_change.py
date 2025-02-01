# 860. Lemonade Change
# https://leetcode.com/problems/lemonade-change/description/

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            elif bill == 20:
                # 10 + 5
                if tens >= 1 and fives >= 1:
                    tens -= 1
                    fives -= 1
                # 5 + 5 + 5
                elif fives >= 3:
                    fives -= 3
                else:
                    return False

        return True
