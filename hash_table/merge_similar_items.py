# 2363. Merge Similar Items
# https://leetcode.com/problems/merge-similar-items/description/
from collections import Counter
from itertools import chain
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        counter = Counter()
        for value, weight in chain(items1, items2):
            counter[value] += weight
        return sorted(counter.items())


# counter = Counter()
# ret = []
# for item in items1:
#     if item not in counter:
#         counter[item] = 1
#     else:
#         counter[item] += 1

# for item in items2:
#     if item not in counter:
#         counter[item] = 1
#     else:
#         counter[item] += 1

# counter.
