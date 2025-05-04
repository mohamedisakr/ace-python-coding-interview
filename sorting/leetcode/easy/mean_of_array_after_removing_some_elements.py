from statistics import mean
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        percent = int(len(arr) * 0.05)
        trim_arr = arr[percent:-percent]
        return sum(trim_arr) / len(trim_arr)


arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
my_sol = Solution()
print(my_sol.trimMean(arr))

# def trimMean(self, arr: List[int]) -> float:
#     arr.sort()
#     offset = len(arr)//20
#     return mean(arr[offset:-offset])
