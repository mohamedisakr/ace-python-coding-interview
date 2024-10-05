
def find_product(lst):
    n = len(lst)
    if n == 0:
        return []

    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n

    # Fill left_products
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * lst[i - 1]

    # Fill right_products
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * lst[i + 1]

    # Fill result
    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result


arr = [1, 2, 3, 4]
# index = 0
# total = prod(arr, index)
# print(f'array product without index # {index} is {total}')

res = find_product(arr)
print(res)
# print(f'arr length is: {len(res)}')

arr1 = [4, 2, 1, 5, 0]
res1 = find_product(arr1)
print(res1)

'''
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
'''
