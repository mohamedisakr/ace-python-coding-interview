class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'

        is_negative = num < 0
        if is_negative:
            num = -num

        ans = []

        while num > 0:
            ans.append(str(num % 7))
            num //= 7

        if is_negative:
            ans.append('-')

        return "".join(reversed(ans))


# if num < 0:
#     return '-' + self.convertToBase7(-num)
