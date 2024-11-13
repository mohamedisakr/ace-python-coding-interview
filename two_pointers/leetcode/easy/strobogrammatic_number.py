# 246. Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/description/


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # Mapping of strobogrammatic numerals where the key is the numeral as int
        # and the value is its 180-degree rotated equivalent (also as an int).
        # Any numeral that doesn't have a strobogrammatic equivalent is mapped to -1.
        # mapper = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6]
        mapper = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        # Pointers to traverse from both ends of the string.
        lo, hi = 0, len(num) - 1

        # Loop to check the strobogrammatic property of the number.
        while lo <= hi:
            left, right = int(num[lo]), int(num[hi])

            if left not in mapper or mapper[left] != right:
                return False

            lo += 1
            hi -= 1

        return True
