def remove_even(lst):
    for x in lst[:]:  # Iterate over a copy of the list
        if x % 2 == 0:
            lst.remove(x)
    return lst


# Test case
my_list = [1, 2, 4, 5, 10, 6, 3]
print(remove_even(my_list))


def remove_even(lst):
    """

    """
    # return [item for item in lst if item % 2 != 0]
    # return (x for x in lst if x % 2 != 0)
    lst[:] = [x for x in lst if x % 2 != 0]
    return lst


my_list = [1, 2, 4, 5, 10, 6, 3]
print(remove_even(my_list))

# Parallel processing
'''
from concurrent.futures import ProcessPoolExecutor


def is_odd(x):
    return x % 2 != 0


def remove_even(lst):
    with ProcessPoolExecutor() as executor:
        result = list(executor.map(is_odd, lst))
    return [x for x, keep in zip(lst, result) if keep]


if __name__ == "__main__":
    my_list = [1, 2, 4, 5, 10, 6, 3]
    print(remove_even(my_list))
'''


'''
def remove_even(lst):
    # using extra space
    evens = list([])
    n = len(lst)
    for i in range(n):
        if lst[i] % 2 != 0:
            evens.append(lst[i])
    return evens
'''
