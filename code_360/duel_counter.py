from collections import defaultdict
from typing import *


def countDuels(n: int, a: List[int]) -> int:
    dic = defaultdict(int)
    duels = 0

    for num in a:
        dic[num] += 1

    processed = set()
    for num in a:
        if num in processed:
            continue
        opposite = -1 * num
        if opposite in dic:
            if num == 0:
                duels += dic[num] * (dic[num] - 1) // 2
            else:
                duels += dic[num] * dic[opposite]

            processed.add(num)
            processed.add(opposite)

    return duels

    # for i in range(n):
    #     if a[i] not in dic:
    #         dic[a[i]] = True

    #     if (a[i] in dic) and ((-1 * a[i]) in dic):
    #         duels += 1

    # return duels
