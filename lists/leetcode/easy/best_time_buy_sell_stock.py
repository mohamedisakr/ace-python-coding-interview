# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update the minimum price
            if price < min_price:
                min_price = price

            # Calculate the profit if selling at the current price
            profit = price - min_price

            # Update the maximum profit
            if profit > max_profit:
                max_profit = profit

        return max_profit


# Example usage:
solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
print(solution.maxProfit([7, 6, 4, 3, 1]))    # Output: 0


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         left, right = 0, n-1
#         # profit = 0
#         min_price, max_price = 1000000, -1000000

#         while left <= right:
#             if min_price < prices[left]:
#                 min_price = prices[left]

#             if max_price > prices[right]:
#                 max_price = prices[right]

#                 left += 1
#                 right -= 1

#         return max((max_price-min_price), 0)


# sol = Solution()
# input_arr = [7, 1, 5, 3, 6, 4]
# profit = sol.maxProfit(input_arr)
# print(f'profit :{profit}')
