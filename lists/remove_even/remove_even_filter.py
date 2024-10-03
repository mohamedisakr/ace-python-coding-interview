def remove_even(lst):
    return list(filter(lambda x: x % 2 != 0, lst))


# Test case
my_list = [1, 2, 4, 5, 10, 6, 3]
print(remove_even(my_list))
