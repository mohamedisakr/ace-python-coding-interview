from typing import List


class Solution:
    def unbounded_knapsack(self, weights: List[int], values: List[int], capacity: int) -> int:
        n = len(weights)

        # Create a 1D DP array initialized with 0
        dp = [0] * (capacity + 1)

        for j in range(capacity + 1):  # Iterate over capacities
            for i in range(n):  # Iterate over items
                if weights[i] <= j:
                    dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

        return dp[capacity]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

sol = Solution()
print(sol.unbounded_knapsack(weights, values, capacity))
