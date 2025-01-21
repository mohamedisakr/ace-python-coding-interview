# 1206. Design Skiplist
# https://leetcode.com/problems/design-skiplist/description/
from dataclasses import dataclass
from random import getrandbits


@dataclass
class Node:
    val: int = -1
    next: 'Node' = None
    down: 'Node' = None


class Skiplist:

    def __init__(self):
        self.dummy = Node()

    def search(self, target: int) -> bool:
        current = self.dummy
        while current:
            while current.next and current.next.val < target:
                current = current.next
            if current.next and current.next.val == target:
                return True
            current = current.down
        return False

    def add(self, num: int) -> None:
        nodes = []
        current = self.dummy
        while current:
            while current.next and current.next.val < num:
                current = current.next
            nodes.append(current)
            current = current.down

        can_insert = True
        down = None

        while can_insert and nodes:
            node: Node = nodes.pop()
            node.next = Node(num, node.next, down)
            down = node.next
            can_insert = getrandbits(1) == 0

        # Create a topmost new level dummy that points to the existing dummy.
        if can_insert:
            self.dummy = Node(-1, None, self.dummy)

    def erase(self, num: int) -> bool:
        current = self.dummy
        is_found = False
        while current:
            while current.next and current.next.val < num:
                current = current.next
            if current.next and current.next.val == num:
                current.next = current.next.next
                is_found = True
            current = current.down
        return is_found

        # Your Skiplist object will be instantiated and called as such:
        # obj = Skiplist()
        # param_1 = obj.search(target)
        # obj.add(num)
        # param_3 = obj.erase(num)
