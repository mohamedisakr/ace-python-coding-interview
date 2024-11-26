# 67. Add Binary
# https://leetcode.com/problems/add-binary/description/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin_str = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1

            bin_str.append(str(carry % 2))
            carry //= 2

        return "".join(reversed(bin_str))

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         bin_str = ""
#         carry = 0
#         a, b = a[::-1], b[::-1]
#         m = len(a)
#         n = len(b)

#         for i in range(max(m, n)):
#             digit_a = ord(a[i]) - ord("0") if i < m else 0
#             digit_b = ord(b[i]) - ord("0") if i < n else 0

#             total = digit_a + digit_b+carry
#             char = str(total % 2)
#             bin_str = char + bin_str
#             carry = total // 2

#         if carry:
#             bin_str = "1" + bin_str

#         return bin_str


# i = len(a) - 1
# j = len(b) - 1
# while i >= 0 or j >= 0:
#     if a[i] == b[j]:
#         bin_str += '0'
#     else:
#         bin_str += '1'
#     i -= 1
#     j -= 1
# return bin_str


a = "11"
b = "1"
expected = "100"
sol = Solution()
actual = sol.addBinary(a, b)
print(actual)
print(expected)
print(f'actual = expected: {actual == expected}')
