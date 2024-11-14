class Solution:

    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split())
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


# '''
#     Input: s = "Let's take LeetCode contest"
#     Output: "s'teL ekat edoCteeL tsetnoc"
#              s'teL ekat edoCteeL
# '''
sol = Solution()
phrase = "Let's take LeetCode contest"
print(sol.reverseWords(s=phrase))

# def reverse_word(word: str) -> str:
#     n = len(word)
#     for i in range(n):
#         word[i],  word[n - i - 1] = word[n - i - 1], word[i]
#     return word


# word = "Let's"
# print(reverse_word(word))
