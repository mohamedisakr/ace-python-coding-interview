# 1812. Determine Color of a Chessboard Square
# https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter, digit = coordinates
        return (((ord(letter) - ord('a')) + 1) + int(digit)) % 2 != 0


coordinates = "c7"
sol = Solution()
print(sol.squareIsWhite(coordinates))


# alpha_numeric = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
#                  'e': 5, 'f': 6, 'g': 7, 'h': 8}
# x = alpha_numeric[coordinates[0]]
# y = int(coordinates[1])
# if (x+y) % 2 != 0:
#     return True
# return False
