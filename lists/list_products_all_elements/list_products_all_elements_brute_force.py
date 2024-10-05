def prod(arr, index):
    total = 1
    n = len(arr)
    for i in range(n):
        if i != index:
            total *= arr[i]
    return total


def find_product(lst):
    n = len(lst)
    mul_list = []
    for i in range(n):
        mul_list.append(prod(lst, i))
    return mul_list
