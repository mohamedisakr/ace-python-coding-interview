class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        lo = 0

        for hi in range(n):
            if s[hi] == " " or hi == n - 1:
                end = hi if s[hi] != ' ' else hi - 1
                start = lo
                while start < end:
                    s[start], s[end] = s[end], s[start]
                    start += 1
                    end -= 1
                lo = hi + 1

        return ''.join(s)


# Example usage:
solution = Solution()
# Output: "s'teL ekat edoCteeL tsetnoc"
print(solution.reverseWords("Let's take LeetCode contest"))


# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = list(s)
#         n = len(s)
#         lo = 0

#         for hi in range(n):
#             if s[hi] == " " or hi == n-1:
#                 temp_lo, temp_hi = lo, hi-1

#                 if temp_hi == n-1:
#                     temp_hi = hi

#                 while temp_lo < temp_hi:
#                     s[temp_lo], s[temp_hi] = s[temp_hi], s[temp_lo]
#                     temp_lo += 1
#                     temp_hi -= 1
#                 lo = hi+1
#         return ''.join(s)


# Example usage:
solution = Solution()
# Output: "s'teL ekat edoCteeL tsetnoc"
print(solution.reverseWords("Let's take LeetCode contest"))

# def reverse(self, s: list, left: int, right: int) -> str:
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
#     return s

# '''
#     Input: s = "Let's take LeetCode contest"
#     Output: "s'teL ekat edoCteeL tsetnoc"
#              s'teL ekat edoCteeL
# '''
# sol = Solution()
# phrase = "Let's take LeetCode contest"
# print(sol.reverseWords(s=phrase))

# def reverse_word(word: str) -> str:
#     n = len(word)
#     for i in range(n):
#         word[i],  word[n - i - 1] = word[n - i - 1], word[i]
#     return word


# word = "Let's"
# print(reverse_word(word))

# first attempt
# n = len(s)
# # space_pos = 0
# word = ''
# rev_txt = ''
# for i in range(n):
#     if s[i] != " ":
#         word += s[i]
#     else:
#         rev_txt += word[::-1]  # reversed(word)
#         rev_txt += " "
#         word = ''
#         # space_pos = i
# return rev_txt
