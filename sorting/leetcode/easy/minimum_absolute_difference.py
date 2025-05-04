from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        n = len(arr)
        pairs = []

        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            if min_diff > diff:
                min_diff = diff
                pairs = [[arr[i], arr[i + 1]]]
            elif min_diff == diff:
                pairs.append([arr[i], arr[i + 1]])

        return pairs
