# 405. Convert a Number to Hexadecimal
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        hex_chars = '0123456789abcdef'
        hex_str = []

        if num < 0:
            num += 2**32

        while num > 0:
            hex_str.append(hex_chars[num & 0xF])
            num >>= 4

        return ''.join(reversed(hex_str))

# class Solution:
#     def toHex(self, num: int) -> str:
#         if num == 0:
#             return "0"

#         hex_chars = "0123456789abcdef"
#         hex_str = []

#         for i in range(7, -1, -1):
#             curr_bits = (num >> (4 * i)) & 0xF

#             if hex_str or curr_bits != 0:
#                 hex_str.append(hex_chars[curr_bits])

#         return "".join(hex_str)
