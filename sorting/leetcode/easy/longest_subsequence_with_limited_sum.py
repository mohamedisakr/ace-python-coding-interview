from bisect import bisect_right
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        cumulative_sum = 0
        prefix_sum = []

        for num in nums:
            cumulative_sum += num
            prefix_sum.append(cumulative_sum)

        answer = []

        for query in queries:
            index = bisect_right(prefix_sum, query)
            answer.append(index)

        return answer


# Input: nums = [4,5,2,1], queries = [3,10,21]
# Output: [2,3,4]
nums = [4, 5, 2, 1]
queries = [3, 10, 21]
sol = Solution()
answer = sol.answerQueries(nums, queries)
print(answer)

# def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
#         answer = [0] * len(queries)
#         for i, q in enumerate(queries):
#             running_total = 0
#             size = 0
#             for j, n in enumerate(nums):
#                 running_total += n
#                 size += 1
#                 if running_total > q:
#                     answer.append(size)
#                     break
#         return answer
# n = len(nums)
# m = len(queries)
# answer = [0] * m
# nums.sort()
# running_total = 0
# j = 0
# size = 0

# for num in nums:
#     running_total += num
#     size += 1
#     if running_total > queries[j]:
#         j += 1
#         break
