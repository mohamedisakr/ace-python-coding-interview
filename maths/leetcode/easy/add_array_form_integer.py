from typing import List


class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        for i in reversed(range(len(num))):
            k, num[i] = divmod(num[i] + k, 10)

        while k > 0:
            num = [k % 10] + num
            k //= 10

        return num

# class Solution:
#     def addToArrayForm(self, num: List[int], k: int) -> List[int]:
#         i, j = len(num) - 1, len(str(k)) - 1
#         carry = 0
#         ans = []

#         while i >= 0 or j >= 0 or carry:
#             if i >= 0:
#                 carry += num[i]

#             if j >= 0:
#                 carry += k % 10

#             ans.append(carry % 10)
#             carry //= 10
#             i -= 1
#             j -= 1

#         return ans[::-1]
