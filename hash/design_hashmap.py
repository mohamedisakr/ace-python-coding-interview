# 706. Design HashMap
# https://leetcode.com/problems/design-hashmap/description/
class Node:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.size = 10**4
        self.map = [Node() for i in range(self.size)]

    def hash(self, key):
        return key % self.size  # len(self.map)

    def put(self, key: int, value: int) -> None:
        current = self.map[self.hash(key)]
        while current.next:
            if current.next.key == key:
                current.next.val = value
                return
            current = current.next
        current.next = Node(key, value)

    def get(self, key: int) -> int:
        current = self.map[self.hash(key)]
        while current:
            if current.key == key:
                return current.val
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        current = self.map[self.hash(key)]
        while current and current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
