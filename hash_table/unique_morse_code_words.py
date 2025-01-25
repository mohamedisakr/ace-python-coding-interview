# 804. Unique Morse Code Words
# https://leetcode.com/problems/unique-morse-code-words/description/
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_map = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                     "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        transformations = set()

        for word in words:
            word_trans = ''.join(morse_map[ord(ch) - ord('a')] for ch in word)
            transformations.add(word_trans)

        return len(transformations)


# class Solution:
#     def uniqueMorseRepresentations(self, words: List[str]) -> int:
#         transformations = set()
#         code_to_letter = self.build_map()

#         for word in words:
#             word_trans = ""
#             for ch in word:
#                 word_trans += code_to_letter[ch]
#             transformations.add(word_trans)

#         return len(transformations)

#     def build_map(self):
#         letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
#                    "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
#         code_letter = {}
#         current_char = "a"

#         n = len(letters)
#         for i in range(n):
#             code_letter[current_char] = letters[i]
#             current_char = chr(ord(current_char) + 1)

#         return code_letter


sol = Solution()
# print(sol.build_map())
words = ["a"]  # ["gin", "zen", "gig", "msg"]
print(sol.uniqueMorseRepresentations(words))
