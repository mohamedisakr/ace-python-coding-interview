def remove_even(lst):
    evens = list([])
    n = len(lst)
    for i in range(n):
        if lst[i] % 2 != 0:
            evens.append(lst[i])
    return evens


my_list = [1, 2, 4, 5, 10, 6, 3]
print(remove_even(my_list))
