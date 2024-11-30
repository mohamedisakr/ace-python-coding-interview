# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            if n >> i & 1:
                ans |= 1 << 31 - i

        return ans

# class Solution:
#     def reverseBits(self, n: int) -> int:
#         rev_bits = 0
#         for i in range(32):
#             rev_bits |= (n & 1) << (31 - i)
#             n >>= 1
#         return rev_bits
