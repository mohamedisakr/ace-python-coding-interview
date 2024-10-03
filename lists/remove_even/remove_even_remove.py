def remove_even(lst):
    for x in lst[:]:  # Iterate over a copy of the list
        if x % 2 == 0:
            lst.remove(x)
    return lst


# Test case
my_list = [1, 2, 4, 5, 10, 6, 3]
print(remove_even(my_list))
