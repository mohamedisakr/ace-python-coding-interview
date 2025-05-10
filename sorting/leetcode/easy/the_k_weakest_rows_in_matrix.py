from bisect import bisect_right
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        soldiers = [rows - bisect_right(row[::-1], 0) for row in mat]
        indices = list(range(rows))
        indices.sort(key=lambda i: soldiers[i])
        return indices[:k]
