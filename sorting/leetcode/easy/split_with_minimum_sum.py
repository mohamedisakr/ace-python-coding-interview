class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(map(int, str(num)))
        num1, num2 = "", ""
        for index, digit in enumerate(digits):
            if index % 2 == 0:
                num1 += str(digit)
            else:
                num2 += str(digit)
        return int(num1) + int(num2)


num = 687  # 4325
sol = Solution()
print(sol.splitNum(num))
