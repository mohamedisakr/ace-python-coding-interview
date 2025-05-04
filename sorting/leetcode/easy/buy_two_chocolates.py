import math
from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = math.inf
        min2 = math.inf

        for price in prices:
            if price <= min1:
                min2 = min1
                min1 = price
            elif price < min2:
                min2 = price

        return money if (min1 + min2) > money else money - (min1 + min2)


# def buyChoco(self, prices: List[int], money: int) -> int:
#     prices.sort()
#     if (prices[0] + prices[1]) <= money:
#         return money - (prices[0] + prices[1])
#     return money
