# import arrays.core as core
# from arrays.core import Array
# from array import array
from array import array
from typing import Union


class SortedArray:
    def __init__(self, max_size, typecode='l'):
        self._array = array(typecode, [0] * max_size)
        self._max_size = max_size
        self._size = 0

    def insert(self, value):
        if self._size >= self._max_size:
            raise ValueError(f"The array is already full, maximum size: {
                             self._max_size}")
        for i in range(self._size, 0, -1):
            if self._array[i-1] <= value:
                self._array[i] = value
                self._size += 1
                return
            else:
                self._array[i] = self._array[i-1]

        self._array[0] = value
        self._size += 1

    def search(self, target):
        for i in range(self._size):
            if self._array[i] == target:
                return i
        return None

    def delete(self, target):
        index = self.search(target)
        if index is None:
            raise ValueError(f'Unable to delete element {
                             target}: the entry is not in the array')

        for i in range(index, self._size-1):
            self._array[i] = self._array[i+1]
        self._size -= 1
