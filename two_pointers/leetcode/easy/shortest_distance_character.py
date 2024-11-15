# 821. Shortest Distance to a Character
# https://leetcode.com/problems/shortest-distance-to-a-character/description/

from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [n] * n

        leftward = float('-inf')
        for i, char in enumerate(s):
            if char == c:
                leftward = i

            answer[i] = min(answer[i], i - leftward)

        rightward = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                rightward = i

            answer[i] = min(answer[i], rightward - i)

        return answer


# Example usage:
solution = Solution()
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]
print(solution.shortestToChar("loveleetcode", 'e'))


# class Solution:
#     def shortestToChar(self, s: str, c: str) -> List[int]:
#         n = len(s)
#         answer = [n]*n
#         distance = 0

#         for i in range(n):
#             if s[i] != c:
#                 distance += 1
#             else:
#                 answer.append(distance)
#                 distance = 0
#         return answer
