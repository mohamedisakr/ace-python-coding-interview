from array import array
# from typing import Optional, Union


class DynamicArray:
    def __init__(self, initial_capacity: int = 1, typecode='l'):
        self._array = array(typecode, [0] * initial_capacity)
        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode

    def resize(self, factor: int = 2) -> None:
        # double capacity
        self._capacity *= factor
        # copy the original array
        original_array = self._array[:]
        # expand max_size array
        self._array = [0] * (self._capacity)
        # copy old array items to the newly one (one by one)
        self._array = original_array[:]

    def insert(self, value):
        if self._size >= self._capacity:
            self.resize()

        self._array[self._size + 1] = value

    # def delete(self, target):
    #     index = self.binary_search(target)
    #     if index is None:
    #         raise ValueError(f'Unable to delete element {
    #                          target}: the entry is not in the array')

    #     for i in range(index, self._size-1):
    #         self._array[i] = self._array[i+1]
    #     self._size -= 1
