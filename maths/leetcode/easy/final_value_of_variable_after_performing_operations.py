# 2011. Final Value of Variable After Performing Operations
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        plus, minus = 0, 0
        for ops in operations:
            if ops in ["++X", "X++"]:
                plus += 1
            if ops in ["--X", "X--"]:
                minus += 1
        return plus - minus


sol = Solution()
operations = ["X++", "++X", "--X", "X--"]
print(sol.finalValueAfterOperations(operations))
