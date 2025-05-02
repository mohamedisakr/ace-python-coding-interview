from collections import defaultdict
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        arr1_counter = defaultdict(int)
        arr1_diff = []

        for value in arr1:
            if value not in arr2_set:
                arr1_diff.append(value)
            arr1_counter[value] += 1

        arr1_diff.sort()

        final_arr = []

        for item in arr2:
            for _ in range(arr1_counter[item]):
                final_arr.append(item)

        return final_arr + arr1_diff
