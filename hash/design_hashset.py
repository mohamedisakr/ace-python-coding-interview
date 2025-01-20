# 705. Design HashSet
# https://leetcode.com/problems/design-hashset/description/

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self._size = 10**4
        self._set = [Node(0) for i in range(self._size)]

    def add(self, key: int) -> None:
        index = key % len(self._set)
        current = self._set[index]
        while current.next:
            if current.next.key == key:
                return
            current = current.next
        current.next = Node(key)

    def remove(self, key: int) -> None:
        index = key % len(self._set)
        current = self._set[index]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

    def contains(self, key: int) -> bool:
        index = key % len(self._set)
        current = self._set[index]
        while current.next:
            if current.next.key == key:
                return True
            current = current.next
        return False

        # Your MyHashSet object will be instantiated and called as such:
        # obj = MyHashSet()
        # obj.add(key)
        # obj.remove(key)
        # param_3 = obj.contains(key)
