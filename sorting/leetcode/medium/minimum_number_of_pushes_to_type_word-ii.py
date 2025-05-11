from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        sorted_counter = sorted(counter.values(), reverse=True)
        total_pushes = 0

        for i, count in enumerate(sorted_counter):
            push_cost = (i // 8) + 1
            total_pushes += count * push_cost

        return total_pushes


word = "aabbccddeeffgghhiiiiii"  # "xyzxyzxyzxyz"  # "abcde"
sol = Solution()
print(sol.minimumPushes(word))
