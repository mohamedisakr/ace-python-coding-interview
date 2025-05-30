class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j = 0, 0
        merged = []

        while i < m and j < n:
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        merged.append(word1[i:])
        merged.append(word2[j:])

        return "".join(merged)

# while i == m and j < n:
#     merged.append(word2[j])
#     j += 1


# while j == n and i < m:
#     merged.append(word1[i])
#     i += 1
# word1 = "abc"
# word2 = "pqr"
word1 = "ab"
word2 = "pqrs"
sol = Solution()
merged = sol.mergeAlternately(word1, word2)
print(merged)
cor = "apbqrs"  # "apbqcr"
print(f'The result is: {merged == cor}')
