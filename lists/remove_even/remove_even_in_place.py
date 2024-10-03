def remove_even(lst):
    lst[:] = [x for x in lst if x % 2 != 0]
    return lst


my_list = [1, 2, 4, 5, 10, 6, 3]
print(remove_even(my_list))
