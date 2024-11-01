from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1]+digits

    # def plusOne(self, digits: List[int]) -> List[int]:
    #     result = int(''.join(map(str, digits)))
    #     result += 1
    #     arr = [int(digit) for digit in str(result)]
    #     return arr


# digits = [9]  # [4, 3, 2, 1]  # [1, 2, 3]
# caller = Solution()
# num = caller.plusOne(digits)
# print(num)
