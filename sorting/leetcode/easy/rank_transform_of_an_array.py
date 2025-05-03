from collections import defaultdict
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        ranking = {val: index + 1 for index, val in enumerate(sorted_unique)}
        return [ranking[num] for num in arr]


arr = [40, 10, 20, 30]
# Output: [4,1,2,3]
my_sol = Solution()
print(my_sol.arrayRankTransform(arr))


# def arrayRankTransform(self, arr: List[int]) -> List[int]:
#     original_postions = {val: index for index, val in enumerate(arr)}
#     print(original_postions)
#     return [4, 6]
