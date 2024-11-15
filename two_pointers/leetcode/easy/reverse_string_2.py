
# 541. Reverse String II
# https://leetcode.com/problems/reverse-string-ii/description/

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        n = len(chars)

        for i in range(0, n, 2*k):
            chars[i:i+k] = reversed(chars[i:i+k])
        return ''.join(chars)


def foo():
    # Convert the input string to a list of characters for in-place modification.
    chars = list(s)

    # Process the list in blocks of 2k characters.
    for i in range(0, len(chars), 2*k):
        # Reverse the first k characters in the current block.
        # If the block is smaller than k, reverse the entire block.
        chars[i: i + k] = reversed(chars[i: i + k])

    # Join the list of characters back into a string and return it.
    return ''.join(chars)
