# 1436. Destination City
# https://leetcode.com/problems/destination-city/description/
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        path_set = set()

        for path in paths:
            path_set.add(path[0])

        for path in paths:
            if path[1] not in path_set:
                return path[1]
