# 1763. Longest Nice Substring
# https://leetcode.com/problems/longest-nice-substring/description/
class Solution:
    """ Optimized divide-and-conquer approach
    """

    def longestNiceSubstring(self, s: str) -> str:
        def helper(start: int, end: int) -> str:
            if end - start < 2:
                return ""

            char_set = set(s[start:end])
            for i in range(start, end):
                char = s[i]
                if char.lower() not in char_set or char.upper() not in char_set:
                    left = helper(start, i)
                    right = helper(i + 1, end)
                    return left if len(left) >= len(right) else right

            return s[start:end]

        return helper(0, len(s))


# class Solution:
#     """ divide-and-conquer approach
#     """

#     def longestNiceSubstring(self, s: str) -> str:
#         def helper(s: str) -> list:
#             n = len(s)
#             if n < 2:
#                 return ""

#             for i, c in enumerate(s):
#                 if c.lower() not in s or c.upper() not in s:
#                     left = helper(s[:i])
#                     right = helper(s[i + 1:])
#                     return left if len(left) >= len(right) else right
#             return s

#         return helper(s)

# class Solution:
#     """ brute force
#     """

#     def longestNiceSubstring(self, s: str) -> str:
#         def is_nice(substring: str) -> bool:
#             char_set = set(substring)

#             for char in substring:
#                 if char.lower() not in char_set or char.upper() not in char_set:
#                     return False
#             return True

#         def generate_all_substrings(s: str) -> list:
#             n = len(s)
#             longest_nice = ""

#             for start in range(n):
#                 for end in range(start + 1, n + 1):
#                     current_str = s[start: end]
#                     if is_nice(current_str) and len(current_str) > len(longest_nice):
#                         longest_nice = current_str
#             return longest_nice

#         return generate_all_substrings(s)
