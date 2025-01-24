# 2325. Decode the Message
# https://leetcode.com/problems/decode-the-message/description/

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        substitution = {' ': ' '}
        curr_char = 'a'
        for char in key:
            if char not in substitution:
                substitution[char] = curr_char
                curr_char = chr(ord(curr_char) + 1)
        return "".join(substitution[char] for char in message)

# return ''.join(keyToActual[c] for c in message)

# key_set = set()
# for ch in key:
#     key_set.add(ch)

# # create hashmap key -> from key_set, value -> from alphabet
# substitution = {}
# unicode_char = 97
# for ch in key_set:
#     substitution[ch] = chr(unicode_char)
#     unicode_char += 1

# print(substitution)


sol = Solution()
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
sol.decodeMessage(key, message)


# print(ord('a'))
# print(chr(97))
