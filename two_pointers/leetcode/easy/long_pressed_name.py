# 925. Long Pressed Name
# https://leetcode.com/problems/long-pressed-name/description/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        i = 0

        for j, char in enumerate(typed):
            if i < n and name[i] == char:
                i += 1
            elif j == 0 or char != typed[j - 1]:
                return False

        return i == n

# class Solution:
#     def isLongPressedName(self, name: str, typed: str) -> bool:
#         m, n = len(name), len(typed)
#         i, j = 0, 0

#         while i < m and j < n:
#             if name[i] != typed[j]:
#                 return False

#             name_count, typed_count = 0, 0

#             curr_char = name[i]

#             while i + 1 < m and name[i + 1] == curr_char:
#                 i += 1
#                 name_count += 1

#             while j + 1 < n and typed[i + 1] == curr_char:
#                 j += 1
#                 typed_count += 1

#             if name_count > typed_count:
#                 return False
