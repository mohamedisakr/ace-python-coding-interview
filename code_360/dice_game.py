from collections import Counter
from typing import List


def minimumOperations(v: List[int]) -> int:
    mismatches = 0

    if v[0] != v[3]:
        mismatches += 1
    if v[1] != v[4]:
        mismatches += 1
    if v[2] != v[5]:
        mismatches += 1

    if mismatches == 0:
        return 0
    elif mismatches == 2:
        return 1
    elif mismatches == 1:
        return 1
    else:  # mismatches == 3
        return 2

    # mismatch = 0
    # if v[0] != v[3]:
    #     mismatch += 1
    # elif v[1] != v[4]:
    #     mismatch += 1
    # elif v[2] != v[5]:
    #     mismatch += 1

    # if mismatch == 0:
    #     return 0
    # elif mismatch == 1:
    #     return 1
    # elif mismatch == 2:
    #     return 1
    # else:
    #     return 2

    # pairs = [(0, 3), (1, 4), (2, 5)]
    # mismatch = []
    # for i, j in pairs:
    #     if v[i] != v[j]:
    #         mismatch.append((i, j))

    # if not mismatch:
    #     return 0

    # if len(mismatch) == 1:
    #     return 1

# def minimumOperations(v: List[int]) -> int:
#     opposite_pairs = [(0, 3), (1, 4), (2, 5)]
#     freq = Counter(v)
#     best_target = max(freq, key=freq.get)
#     swaps_needed = 0

#     for i, j in opposite_pairs:
#         if best_target not in (v[i], v[j]):
#             swaps_needed += 1
#         elif v[i] != best_target or v[j] != best_target:
#             swaps_needed += 1

#     return swaps_needed

# def minimumOperations(v: List[int]) -> int:
#     opposite_pairs = [(0, 3), (1, 4), (2, 5)]

#     swaps_needed = 0

#     for i, j in opposite_pairs:
#         possible_targets = {v[i], v[j]}  # Consider both values
#         best_target = max(possible_targets, key=lambda x: v.count(x))

#         if best_target not in (v[i], v[j]):
#             swaps_needed += 1
#         elif v[i] != best_target or v[j] != best_target:
#             swaps_needed += 1

#     return swaps_needed

# def minimumOperations(v: List[int]) -> int:
#     opposite_pairs = [(0, 3), (1, 4), (2, 5)]
#     swaps = 0

#     for i, j in opposite_pairs:
#         vals = [v[i], v[j]]
#         best_target = max(vals, key=lambda x: v.count(x))

#         if v[i] != best_target or v[j] != best_target:
#             swaps += 1

#     return swaps


# v = [1, 2, 3, 1, 2, 3]
v = [10, 2, 2, 2, 2, 10]
print(minimumOperations(v))
