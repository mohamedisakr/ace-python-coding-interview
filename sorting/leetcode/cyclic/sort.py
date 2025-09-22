def cyclic_sort(arr: list[int]) -> list[int]:
    """
    Sorts an array of positive integers in-place using the Cyclic Sort algorithm.

    This algorithm is highly efficient for arrays that contain numbers in a
    specific range, typically from 1 to n, where n is the length of the array.
    The core idea is to place each number at its correct index.

    The correct position for an element `x` in a 1-to-n range is at index `x - 1`.

    Args:
        arr: A list of integers to be sorted. It is assumed that the list contains
             numbers from 1 to n (where n is the list's length).

    Returns:
        The sorted list. The sorting is done in-place, so the original list
        is also modified.

    Example:
        >>> cyclic_sort([3, 1, 5, 2, 4])
        [1, 2, 3, 4, 5]
    """
    length = len(arr)
    for i in range(length):
        while arr[i] != i + 1:
            index = arr[i] - 1
            arr[i], arr[index] = arr[index], arr[i]
    return arr


# Driver code
def main():
    nums = [
        [1, 3, 2, 5, 4],
        [2, 4, 5, 1, 3],
        [1, 2, 4, 3],
        [3, 1, 5, 6, 4, 2]
    ]
    for i in range(len(nums)):
        print(i + 1, ".\tArray before cyclic sort = ", nums[i], sep="")
        print("\tArray after cyclic sort = ", cyclic_sort(nums[i]), sep="")
        print("-" * 85)


def missing():
    nums = [
        [1],
        # [1, 2, 0],
        [4, 2, 3, 1],
        [8, 3, 5, 2, 4, 6, 7, 1]
    ]

    for i in range(len(nums)):
        print(i + 1, ".\tArray before cyclic sort = ", nums[i], sep="")
        print("\tArray after cyclic sort = ", cyclic_sort(nums[i]), sep="")
        print("-" * 85)


if __name__ == '__main__':
    # main()
    missing()
