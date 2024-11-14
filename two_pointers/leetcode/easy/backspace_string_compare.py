# 844. Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/description/


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_valid_index(text, index):
            backspaces = 0
            while index >= 0:
                if text[index] == '#':
                    backspaces += 1
                elif backspaces > 0:
                    backspaces -= 1
                else:
                    break
                index -= 1
            return index

        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = next_valid_index(s, i)
            j = next_valid_index(t, j)

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            if (i >= 0) != (j >= 0):
                return False

            i -= 1
            j -= 1

        return True


solution = Solution()
print(solution.backspaceCompare("ab#c", "ad#c"))  # Output: True
print(solution.backspaceCompare("ab##", "c#d#"))  # Output: True
print(solution.backspaceCompare("a#c", "b"))  # Output: False

# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         def remove_backspaces(text: str) -> str:
#             storage = []
#             for char in text:
#                 if char != '#':
#                     storage.append(char)
#                 elif storage:
#                     storage.pop()
#             return ''.join(storage)

#         return remove_backspaces(s) == remove_backspaces(t)

# def build_final_string(s: str) -> str:
#     stack = []
#     for char in s:
#         if char != '#':
#             stack.append(char)
#         elif stack:
#             stack.pop()
#     return ''.join(stack)


# s = "ab##"
# t = "c#d#"
# result = build_final_string(s) == build_final_string(t)
# print(result)

# def build_final_string(s: str) -> str:
#     stack = []
#     for char in s:
#         if char != '#':
#             stack.append(char)
#         elif stack:
#             stack.pop()
#         return ''.join(stack)


# def backspaceCompare(self, s: str, t: str) -> bool:
#         from re import sub

#         first = sub(r'.#', '', s)
#         second = sub(r'.#', '', t)

#         return first == second

# s = "ab##"
# t = "c#d#"
# result = re.sub(r'.#', '', s)
# print(result)
