# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/description/

from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]

        max_heap = [-stone for stone in stones]
        heapify(max_heap)

        while len(max_heap) > 1:
            first = -heappop(max_heap)
            second = -heappop(max_heap)

            if first != second:
                heappush(max_heap, -(first - second))

        return 0 if not max_heap else -max_heap[0]
