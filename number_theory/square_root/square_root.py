def sqr_root(num: int) -> int | None:
    if num < 0:
        return None
    if num in (0, 1):
        return num

    lo, hi = 1, num

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        square = mid * mid

        if square == num:
            return mid
        elif square < num:
            lo = mid + 1
        else:
            hi = mid - 1

    return None

# def sqr_root(num: int):
#     guess = 0

#     while guess ** 2 < num:
#         guess += 1

#     if guess ** 2 == num:
#         print(f"Square root of {num} is {guess}")
#     else:
#         print(f"{num} is not a perfect square")
