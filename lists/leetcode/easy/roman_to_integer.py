class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dic = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        n = len(s)

        for i in range(n):
            if i+1 < n and roman_dic[s[i]] < roman_dic[s[i+1]]:
                total -= roman_dic[s[i]]
            else:
                total += roman_dic[s[i]]

        return total


sol = Solution()
print(sol.romanToInt('III'))


# roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# txt = 'MCMXCIV'
# n = len(txt)
# total = 0
# for i in range(n):
#     if txt[i:3] in roman_dic:
#         total += roman_dic[txt[i:3]]
#         print(f'the number is {total}')


# 'IX': 4,
# 'IV': 9,
# 'XL': 40,
# 'XC': 90,
# 'CD': 400,
# 'Cm': 900,
