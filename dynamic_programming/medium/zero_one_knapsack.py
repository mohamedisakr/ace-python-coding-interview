from typing import List


class Solution:
    def knapsack_optimized(self, weights: List[int], values: List[int], capacity) -> int:
        n = len(weights)

        # Use two 1D arrays to store the current and previous rows
        # Represents the previous row in the DP table
        prev = [0] * (capacity + 1)
        # Represents the current row in the DP table
        curr = [0] * (capacity + 1)

        for i in range(1, n + 1):  # Iterate over items
            for j in range(capacity + 1):  # Iterate over capacities
                if weights[i - 1] <= j:
                    # If the item can fit, choose the maximum between:
                    # 1. Excluding the item (prev[j])
                    # 2. Including the item (prev[j - weights[i - 1]] + values[i - 1])
                    curr[j] = max(
                        prev[j], prev[j - weights[i - 1]] + values[i - 1])
                else:
                    # If the item cannot fit, exclude it
                    curr[j] = prev[j]
            # Update the previous row to be the current row
            prev, curr = curr, [0] * (capacity + 1)

        return prev[capacity]
