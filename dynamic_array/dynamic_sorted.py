from array import array


class DynamicSortedArray:
    def __init__(self, initial_capacity: int = 1, typecode='l'):
        self._array = array(typecode, [0] * initial_capacity)
        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode

    def resize(self, factor: int = 2) -> None:
        # Double capacity or use provided factor
        self._capacity = int(self._capacity * factor)
        new_array = array(self._typecode, [0] * self._capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

    def insert(self, value):
        if self._size >= self._capacity:
            self.resize()
        # 10, 20 -- 5
        # Optimized insertion point search
        index = 0
        while index < self._size and self._array[index] < value:
            index += 1

        # Shift elements to make space
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]

        self._array[index] = value
        self._size += 1

    def binary_search(self, target):
        lo = 0
        hi = self._size - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self._array[mid] == target:
                return mid
            elif self._array[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return None

    def half_size(self, factor: int = 2):
        self._capacity = max(1, int(self._capacity / factor))
        new_array = array(self._typecode, [0] * self._capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

    def delete(self, target):
        index = self.binary_search(target)
        if index is None:
            raise ValueError(f'Unable to delete element {
                             target}: the entry is not in the array')
        # 1, 2, 3, 4, 5
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]

        self._size -= 1

        if self._size <= self._capacity / 4:
            self.half_size()


# # ----- non optimized -------
# from array import array


# class DynamicSortedArray:
#     def __init__(self, initial_capacity: int = 1, typecode='l'):
#         self._array = array(typecode, [0] * initial_capacity)
#         self._capacity = initial_capacity
#         self._size = 0
#         self._typecode = typecode

#     def resize(self, factor: int = 2) -> None:
#         # double capacity
#         self._capacity *= factor
#         # create new array with the new capacity
#         new_array = array(self._typecode, [0] * self._capacity)
#         # copy the original array
#         for i in range(self._size):
#             new_array[i] = self._array[i]
#         self._array = new_array

#     def insert(self, value):
#         if self._size == self._capacity:
#             self.resize()
#         # 10, 20 -- 5
#         for i in range(self._size, 0, -1):
#             if self._array[i-1] <= value:
#                 self._array[i] = value
#                 self._size += 1
#                 return
#             else:
#                 self._array[i] = self._array[i-1]

#         self._array[0] = value
#         self._size += 1

#     def linear_search(self, target):
#         for i in range(self._size):
#             if self._array[i] == target:
#                 return i
#             if self._array[i] > target:
#                 return None
#         return None

#     def binary_search(self, target):
#         lo = 0
#         hi = self._size - 1
#         while lo <= hi:
#             mid = lo+(hi-lo)//2
#             val = self._array[mid]
#             if val == target:
#                 return mid
#             elif val > target:
#                 hi = mid - 1
#             else:
#                 lo = mid + 1
#         return None

#     def half_size(self, factor: int = 4):
#         # create new array with the new capacity
#         new_array = array(self._typecode, [0] * int(self._capacity//factor))

#         # copy the original array
#         for i in range(self._size):
#             new_array[i] = self._array[i]
#         self._array = new_array

#     def delete(self, target):
#         index = self.binary_search(target)
#         if index is None:
#             raise ValueError(f'Unable to delete element {
#                              target}: the entry is not in the array')

#         for i in range(index, self._size-1):
#             self._array[i] = self._array[i+1]

#         self._array[self._size-1] = 0
#         self._size -= 1

#         if self._capacity > 1 and self._size <= self._capacity/4:
#             self.half_size()
