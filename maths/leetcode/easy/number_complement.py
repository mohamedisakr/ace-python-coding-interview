# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        # return int(''.join('1' if bit == '0' else '0' for bit in bin(num)[2:]), 2)
        return num ^ (2**(len(bin(num))-2)-1)
