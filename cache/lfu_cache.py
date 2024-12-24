# 460. LFU Cache
# https://leetcode.com/problems/lfu-cache/
from collections import defaultdict


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.freq = 1


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = Node(-1, -1)  # Sentinel head node
        self.tail = Node(-1, -1)  # Sentinel tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_first(self, node: Node) -> None:
        """Add a node right after the head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node: Node) -> Node:
        """Remove an existing node from the list."""
        node.prev.next = node.next
        node.next.prev = node.prev
        # Clear the removed node's pointers
        node.next, node.prev = None, None
        return node

    def remove_last(self) -> Node:
        """Remove the last node and return it."""
        return self.remove(self.tail.prev)

    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.head.next == self.tail


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_node_map = defaultdict(Node)
        self.freq_node_list_map = defaultdict(DoublyLinkedList)

    def get(self, key: int) -> int:
        """Get the value of the key if the key exists in the cache."""
        if self.capacity == 0 or key not in self.key_node_map:
            return -1

        node = self.key_node_map[key]
        self._increase_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """Set or insert the value if the key is not already present."""
        if self.capacity == 0:
            return

        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.value = value
            self._increase_freq(node)
            return

        if len(self.key_node_map) == self.capacity:
            least_freq_list = self.freq_node_list_map[self.min_freq]
            node_to_remove = least_freq_list.remove_last()
            del self.key_node_map[node_to_remove.key]

        new_node = Node(key, value)
        self._add_node(new_node)
        self.key_node_map[key] = new_node
        self.min_freq = 1  # Reset min_freq to 1 as a new node is added

    def _increase_freq(self, node: Node) -> None:
        """Increase the frequency count of a node."""
        freq = node.freq
        node_list = self.freq_node_list_map[freq]
        node_list.remove(node)
        if node_list.is_empty():
            del self.freq_node_list_map[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        node.freq += 1
        self._add_node(node)

    def _add_node(self, node: Node) -> None:
        """Add a node to the list that corresponds to its frequency count."""
        freq = node.freq
        node_list = self.freq_node_list_map[freq]
        node_list.add_first(node)


if __name__ == "__manin__":
    lfu = LFUCache(2)
    lfu.put(1, 1)   # cache=[1,_], cnt(1)=1
    lfu.put(2, 2)   # cache=[2,1], cnt(2)=1, cnt(1)=1
    lfu.get(1)      # return 1
    # cache=[1,2], cnt(2)=1, cnt(1)=2
    # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
    lfu.put(3, 3)
    # cache=[3,1], cnt(3)=1, cnt(1)=2
    lfu.get(2)      # return -1 (not found)
    lfu.get(3)      # return 3
    # cache=[3,1], cnt(3)=2, cnt(1)=2
    # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
    lfu.put(4, 4)
    # cache=[4,3], cnt(4)=1, cnt(3)=2
    lfu.get(1)      # return -1 (not found)
    lfu.get(3)      # return 3
    # cache=[3,4], cnt(4)=1, cnt(3)=3
    lfu.get(4)      # return 4
# cache=[4,3], cnt(4)=2, cnt(3)=3

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


"""
old implementation
"""
# class Node:
#     def __init__(self, key, val, prev=None, nxt=None):
#         self.key = key
#         self.val = val
#         self.prev = prev
#         self.next = nxt
#         self.frequency = 1


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = Node(-1, -1)
#         self.tail = Node(-1, -1)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def add_first(self, node: Node) -> None:
#         """Add a node right after the head."""
#         node.prev = self.head
#         node.next = self.head.next
#         self.head.next.prev = node
#         self.head.next = node

#     def remove(self, node: Node) -> Node:
#         """Remove an existing node from the list."""
#         if node is None:
#             return None

#         if self.is_empty():
#             return None

#         node.prev.next = node.next
#         node.next.prev = node.prev
#         # Clear the removed node's pointers
#         node.next, node.prev = None, None
#         return node

#     def remove_last(self) -> Node:
#         """Remove the last node and return it."""
#         return self.remove(self.tail.prev)

#     def is_empty(self) -> bool:
#         """Check if the list is empty."""
#         return self.head.next == self.tail


# class LFUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.min_freq = 0
#         self.key_node_map = defaultdict(Node)
#         self.freq_node_list_map = defaultdict(DoublyLinkedList)

#     def get(self, key: int) -> int:
#         """Get the value of the key if the key exists in the cache."""
#         if self.capacity == 0 or key not in self.key_node_map:
#             return -1

#         node = self.key_node_map[key]
#         self._increase_freq(node)
#         return node.val

#     def put(self, key: int, value: int) -> None:
#         if self.capacity == 0:
#             return

#         if key in self.key_node_map:
#             node = self.key_node_map[key]
#             node.val = value
#             self._increase_freq(node)
#             return

#         if len(self.key_node_map) == self.capacity:
#             lfu_list = self.freq_node_list_map[self.min_freq]
#             node = lfu_list.remove_last()
#             del self.key_node_map[node.key]

#         new_node = Node(key, value)
#         self._add_node(new_node)
#         self.key_node_map[key] = new_node
#         new_node.frequency = 1

#     def _increase_freq(self, node: Node) -> None:
#         """Increase the frequency count of a node."""
#         freq = node.frequency
#         node_list = self.freq_node_list_map[freq]
#         node_list.remove(node)
#         if node_list.is_empty():
#             del self.freq_node_list_map[freq]
#             if freq == self.min_freq:
#                 self.min_freq += 1

#         node.frequency += 1
#         self._add_node(node)

#     def _add_node(self, node: Node) -> None:
#         """Add a node to the list that corresponds to its frequency count."""
#         freq = node.frequency
#         node_list = self.freq_node_list_map[freq]
#         node_list.add_first(node)
