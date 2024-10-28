from typing import Optional


class Node:
    def __init__(self, value: int, prev: Optional['Node'] = None, next: Optional['Node'] = None):
        self.value: int = value
        self.prev: Optional[Node] = prev
        self.next: Optional[Node] = next

# class Node:
#     def __init__(self, value, previous=None, next=None):
#         self.value = value
#         self.previous = previous
#         self.next = next
