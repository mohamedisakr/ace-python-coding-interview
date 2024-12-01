from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ones = [0] * (n+1)
        for i in range(n + 1):
            ones[i] = i.bit_count()
        return ones
