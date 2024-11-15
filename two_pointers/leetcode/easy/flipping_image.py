# 832. Flipping an Image
# https://leetcode.com/problems/flipping-an-image/description/

from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n_cols = len(image)
        for row in image:
            lo, hi = 0, n_cols-1
            while lo < hi:
                if row[lo] == row[hi]:
                    row[lo] = 1-row[lo]
                    row[hi] = 1-row[hi]
                lo, hi = lo+1, hi-1

            if lo == hi:
                row[lo] = 1-row[lo]

        return image
