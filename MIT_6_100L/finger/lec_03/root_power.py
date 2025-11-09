def find_root_power(x: int) -> tuple[int, int] | None:
    if not isinstance(x, int):
        raise TypeError("Input must be an integer.")

    for root in range(-abs(x), abs(x) + 1):
        for pwr in range(2, 6):
            if root ** pwr == x:
                return root, pwr
    return None


# def find_root_power(num: int) -> tuple[int, int] | None:
#     if not isinstance(num, int):
#         raise TypeError("Input must be an integer.")

#     for pwr in range(2, 6):
#         for root in range(1, abs(num) + 1):
#             if root ** pwr == num:
#                 return root, pwr
#             if (-root) ** pwr == num:
#                 return -root, pwr

#     return None


# def find_root_power(num: int) -> None:
#     found = False
#     for pwr in range(2, 6):
#         for root in range(-abs(num), abs(num) + 1):
#             print(f"root = {root}")
#             if root ** pwr == num:
#                 print(f"root = {root}, pwr = {pwr}")
#                 found = True
#                 return
#     if not found:
#         print("No pair of integers (root, pwr) found such that root**pwr ==", num)


# num = 27
# find_root_power(num)
