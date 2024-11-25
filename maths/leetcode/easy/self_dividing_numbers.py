from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_div = []
        for num in range(left, right + 1, 1):
            if self.check_divide(num):
                self_div.append(num)
        return self_div

    def check_divide(self, num: int):
        number = num
        while number > 0:
            digit = number % 10
            if digit == 0 or num % digit != 0:
                return False
            number //= 10
        return True


# sol = Solution()
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 48, 55, 66, 77]
# for num in nums:
#     print(sol.check_divide(num) == True)


# class Solution:
#     def selfDividingNumbers(self, left: int, right: int) -> list[int]:
#         return [num for num in range(left, right + 1) if all(n != 0 and num % n == 0 for n in map(int, str(num)))]
