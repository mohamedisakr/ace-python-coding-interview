# import arrays.core as core
# from arrays.core import Array
# from array import array
from array import array
from typing import Union


class SortedArray:
    def __init__(self, max_size, typecode='l'):  # 'u'
        # self._array = array(typecode)  # , max_size
        # self._array = core.Array(max_size, typecode)
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
