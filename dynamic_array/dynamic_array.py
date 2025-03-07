# from typing import Optional, Union
from array import array


class DynamicArray:
    def __init__(self, initial_capacity: int = 1, typecode='l'):
        self._array = array(typecode, [0] * initial_capacity)
        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode

    def resize(self, factor: int = 2) -> None:
        # double capacity
        self._capacity *= factor
        # create new array with the new capacity
        new_array = array(self._typecode, [0] * self._capacity)
        # copy the original array
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

    def insert(self, value):
        if self._size == self._capacity:
            self.resize()

        self._array[self._size] = value
        self._size += 1

    def find(self, target):
        for index in range(self._size):
            if self._array[index] == target:
                return index
        return None

    def half_size(self, factor: int = 4):
        # self._capacity //= factor
        # create new array with the new capacity
        new_array = array(self._typecode, [0] * int(self._capacity//factor))
        #
        # copy the original array
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

    def delete(self, target):
        index = self.find(target)
        if index is None:
            raise ValueError(f'Unable to delete element {
                             target}: the entry is not in the array')

        for i in range(index, self._size-1):
            self._array[i] = self._array[i+1]

        self._array[self._size-1] = 0
        self._size -= 1

        if self._capacity > 1 and self._size <= self._capacity/4:
            self.half_size()
