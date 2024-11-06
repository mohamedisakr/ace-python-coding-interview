from array import array


class DynamicSortedArray:
    def __init__(self, initial_capacity: int = 1, typecode='l'):
        self._array = array(typecode, [0] * initial_capacity)
        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode

    def resize(self, factor: int = 2) -> None:
        self._capacity = int(self._capacity * factor)
        new_array = array(self._typecode, [0] * self._capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        print(f"Resized to {self._capacity}")

    def insert(self, value):
        if self._size >= self._capacity:
            self.resize()

        index = 0
        while index < self._size and self._array[index] < value:
            index += 1

        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]

        self._array[index] = value
        self._size += 1
        print(f"Inserted {value}. Current size: {
              self._size}, Capacity: {self._capacity}")

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

    def shrink(self):
        print(f"Attempting to shrink: Current size: {
              self._size}, Current capacity: {self._capacity}")
        if self._capacity > 1 and self._size <= self._capacity // 4:
            new_capacity = max(1, self._capacity // 2)
            self._capacity = new_capacity
            new_array = array(self._typecode, [0] * self._capacity)
            for i in range(self._size):
                new_array[i] = self._array[i]
            self._array = new_array
            print(f"Shrunk down to {self._capacity}")

    def delete(self, target):
        index = self.binary_search(target)
        if index is None:
            raise ValueError(f'Unable to delete element {
                             target}: the entry is not in the array')

        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]

        self._size -= 1
        print(f"Deleted {target}. Current size: {
              self._size}, Capacity: {self._capacity}")

        self.shrink()
