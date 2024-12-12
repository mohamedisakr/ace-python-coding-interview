# 1652. Defuse the Bomb
# https://leetcode.com/problems/defuse-the-bomb/description/
from typing import List
from itertools import accumulate


class Solution:

    """
    Prefix Sums
    """

    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decrypted_code = [0] * n

        if k == 0:
            return decrypted_code

        prefix_sum = list(accumulate(code+code, initial=0))

        for i in range(n):
            if k > 0:
                decrypted_code[i] = prefix_sum[i + k + 1] - prefix_sum[i + 1]
            elif k < 0:
                decrypted_code[i] = prefix_sum[i + n] - prefix_sum[i + k + n]

        return decrypted_code

# class Solution:
#     def decrypt(self, code: list[int], k: int) -> list[int]:
#         n = len(code)
#         ans = [0] * n

#         if k == 0:
#             return ans

#         summ = 0
#         start = 1 if k > 0 else n + k  # the start of the next k numbers
#         end = k if k > 0 else n - 1  # the end of the next k numbers

#         for i in range(start, end + 1):
#             summ += code[i]

#         for i in range(n):
#             ans[i] = summ
#             summ -= code[start % n]
#             start += 1
#             end += 1
#             summ += code[end % n]

#         return ans


# Input: code = [2,4,9,3], k = -2
# Output: [12,5,6,13]
# Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4].
# Notice that the numbers wrap around again.
# If k is negative, the sum is of the previous numbers.

sol = Solution()
# k == 0
# code = [1, 2, 3, 4]
# k = 0
# print(sol.decrypt(code, k))

# k < 0
code = [2, 4, 9, 3]
k = -2
print(code[k])

# k > 0
# code = [5, 7, 1, 4]
# k = 3
# # Output: [12,10,16,13]
# print(sol.decrypt(code, k))


# # If k > 0, replace the ith number with the sum of the next k numbers.
# # Input: code = [5,7,1,4], k = 3
# # Output: [12,10,16,13]
# # Explanation: Each number is replaced by the sum of the next 3 numbers.
# # The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1].
# # Notice that the numbers wrap around.
# elif k > 0:
#     for i in range(n):
#         decrypted_code[i] = sum(code) - code[i]
#     return decrypted_code
# else:
#     # If k < 0, replace the ith number with the sum of the previous k numbers.
#     # Input: code = [2,4,9,3], k = -2
#     # Output: [12,5,6,13]
#     # Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4].
#     # Notice that the numbers wrap around again.
#     # If k is negative, the sum is of the previous numbers.
#     for i in range(n):
#         decrypted_code[i] = sum(code) - code[i]
#     return decrypted_code
