def remove_even(lst):
    return [item for item in lst if item % 2 != 0]


# Test case
my_list = [1, 2, 4, 5, 10, 6, 3]
print(remove_even(my_list))
