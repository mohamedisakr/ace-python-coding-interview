from typing import Optional


class Node:
    def __init__(self, val: int, prev: 'Optional[Node]' = None, nxt: 'Optional[Node]' = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt


def toArray(head: Optional[Node]) -> list[int]:
    ans = []
    curr = head

    while curr:
        ans.append(curr.val)
        curr = curr.nxt

    return ans


# head = [1,2,3,4,3,2,1]
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(3)
sixth = Node(2)
seventh = Node(1)

head.prev = None
head.nxt = second

second.prev = head
second.nxt = third

third.prev = second
third.nxt = fourth

fourth.prev = third
fourth.nxt = fifth

fifth.prev = fourth
fifth.nxt = sixth

sixth.prev = fifth
sixth.nxt = seventh

seventh.prev = sixth
seventh.nxt = None

print(toArray(head))  # [1,2,3,4,3,2,1]
