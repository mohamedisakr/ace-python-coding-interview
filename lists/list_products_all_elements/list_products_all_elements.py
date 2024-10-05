
def find_product(lst):
    n = len(lst)
    product = []

    # get product starting from left
    left = 1

    for item in lst:
        product.append(left)
        left = left * item

    # get product starting from right
    right = 1

    for i in range(n-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


# print(find_product([1, 2, 3, 4]))
