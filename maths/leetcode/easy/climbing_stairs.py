# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description


class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 1
        for i in range(n-1):
            prev, curr = curr, prev + curr
        return curr

    # prev, curr = 0, 1
    #     for i in range(n):
    #         prev, curr = curr, prev+curr
    #     return prev
