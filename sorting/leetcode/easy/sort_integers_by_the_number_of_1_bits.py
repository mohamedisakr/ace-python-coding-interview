from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda n: (n.bit_count(), n))
        return arr
        # return sorted(arr, key=lambda x: (x.bit_count(), x))
