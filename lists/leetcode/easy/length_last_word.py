class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        n = len(s)

        for i in range(n-1, -1, -1):
            if s[i] != ' ':
                length += 1
            elif length > 0:
                break

        return length


# trimmed = s.strip()
        # last_word = trimmed.split()[-1]
        # return len(last_word)
