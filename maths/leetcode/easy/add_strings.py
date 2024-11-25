class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(num1[i])
            if j >= 0:
                carry += int(num2[j])

            ans.append(str(carry % 10))
            carry //= 10
            i -= 1
            j -= 1

        return "".join(reversed(ans))


#     digit_1 = 0 if i < 0 else int(num1[i])
#     digit_2 = 0 if j < 0 else int(num2[j])
#     carry, value = divmod(digit_1+digit_2+carry, 10)
#     ans.append(str(value))
#     i -= 1
#     j -= 1

# return "".join(ans.reverse())
