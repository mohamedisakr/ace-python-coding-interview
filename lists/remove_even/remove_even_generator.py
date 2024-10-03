def remove_even(lst):
    return (x for x in lst if x % 2 != 0)


# To use the generator, you can convert it to a list or iterate over it
my_list = [1, 2, 4, 5, 10, 6, 3]
print(list(remove_even(my_list)))  # Convert to list if needed
