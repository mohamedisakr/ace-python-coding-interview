from math import prod
from typing import List


def find_product(arr: List[int]):
    n = len(arr)
    res = [1] * n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= arr[i]

    suffix = 1
    for i in reversed(range(n)):
        res[i] *= suffix
        suffix *= arr[i]

    return res

# def find_product(arr: List[int]):
#     pre, suf = prefix_product(arr), suffix_product(arr)
#     return [a * b for a, b in zip(pre, suf)]


def prefix_product(arr: List[int]) -> List[int]:
    n = len(arr)
    pre: List[int] = [1] * n

    for i in range(1, n):
        pre[i] = prod(arr[:i])

    return pre


def suffix_product(arr: List[int]) -> List[int]:
    n = len(arr)
    suf: List[int] = [1] * n

    for i in range(n):
        suf[i] = prod(arr[i + 1:])

    return suf


# arr = [1, 2, 3, 4]
# print(f'product: \t{find_product(arr)}')


# print(f'prefix: \t{prefix_product(arr)}')
# print(f'suffix: \t{suffix_product(arr)}')
