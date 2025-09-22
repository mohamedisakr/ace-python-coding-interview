from typing import List


def remove_even_for(arr: List[int]) -> List[int]:
    # [1,2,4,5,10,6,3] --> [1,5,3]
    res: List[int] = []
    for i, item in enumerate(arr):
        if item % 2 != 0:
            res.append(item)
    return res


def remove_even_comprehension(arr: List[int]) -> List[int]:
    return [item for item in arr if item % 2 != 0]


def remove_even_filter(arr: List[int]) -> List[int]:
    return list(filter(lambda item: item % 2 != 0, arr))


def remove_even_generator(arr: List[int]) -> List[int]:
    return list(item for item in arr if item % 2 != 0)


def remove_even_loop(arr: List[int]) -> List[int]:
    for item in arr[:]:
        if item % 2 == 0:
            arr.remove(item)
    return arr


arr = [1, 2, 4, 5, 10, 6, 3]
# res = remove_even_for(arr)
# res = remove_even_comprehension(arr)
# res = remove_even_filter(arr)
# res = remove_even_generator(arr)
res = remove_even_loop(arr)
print(res)
