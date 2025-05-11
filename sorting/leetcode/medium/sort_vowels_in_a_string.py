from collections import defaultdict


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        sorted_vowels = sorted([c for c in s if c in vowels])

        t = []
        i = 0  # sorted vowels index

        for c in s:
            if c in vowels:
                t.append(sorted_vowels[i])
                i += 1
            else:
                t.append(c)

        return "".join(t)


s = "lEetcOde"
sol = Solution()
print(sol.sortVowels(s))

# vowels = ['a', 'e', 'i', 'o', 'u']
# vowels_dic = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

#  vowels = ['a', 'e', 'i', 'o', 'u']
#   vowels_dic = defaultdict()
#    for index, value in enumerate(vowels):
#         vowels_dic[value] = ord(value)
#     print(vowels_dic)

# copilot solution
# class Solution:
#     def sortVowels(self, s: str) -> str:
#         n = len(s)
#         vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#         # Step 1: Extract vowels positions
#         vowel_positions = [i for i in range(n) if s[i] in vowels]
#         # Step 2: Extract vowels & Sort them
#         sorted_vowels = sorted(s[i] for i in vowel_positions)
#         # Step 3: Convert string to list for mutation
#         s_list = list(s)

#         for index, pos in enumerate(vowel_positions):
#             s_list[pos] = sorted_vowels[index]

#         return "".join(s_list)
