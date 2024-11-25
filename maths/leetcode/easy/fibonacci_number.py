class Solution:
    def fib(self, n: int) -> int:
        prev, curr = 0, 1
        for i in range(n):
            prev, curr = curr, prev+curr
        return prev


n = 2
sol = Solution()
print(sol.fib(n) == 1)


# class Solution:
#     def fib(self, n: int) -> int:
#         if n < 2:
#             return n

#         dp = [0, 0, 1]

#         for i in range(2, n + 1):
#             dp[0] = dp[1]
#             dp[1] = dp[2]
#             dp[2] = dp[0] + dp[1]

#         return dp[2]
