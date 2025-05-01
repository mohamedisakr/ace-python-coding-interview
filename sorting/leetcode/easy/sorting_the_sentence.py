class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join([word[:-1] for word in sorted(s.split(), key=lambda x: x[-1])])


s = "is2 sentence4 This1 a3"
sol = Solution()
print(sol.sortSentence(s))

# words = s.split(sep=' ')
#         pos_to_word = {}
#         for index, val in enumerate(words):
#             pos_to_word[val[-1]] = val[0:len(val)-1]
#         print(words)
#         print(pos_to_word)

#         return 'hello'
