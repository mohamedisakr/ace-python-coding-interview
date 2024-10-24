from typing import Any, Optional


class Node():
    def __init__(self, value: Any):
        self.value: Any = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
