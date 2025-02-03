# Tabulation (Bottom-Up DP):
# Build the solution iteratively using a table (array) to store intermediate results.

def fibonacci_tabulation(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
