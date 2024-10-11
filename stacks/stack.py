class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self) -> bool:
        return self.stack_size == 0

    def push(self, value):
        self.stack_list.append(value)
        self.stack_size += 1

    def pop(self):
        if self.is_empty():
            return None
        self.stack_list.pop()
        self.stack_size -= 1

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def capacity(self) -> int:
        return self.stack_size


if __name__ == "__main__":
    stack_obj = MyStack()
    print(f'is_empty: {stack_obj.is_empty()}')
    print(f'peek: {stack_obj.peek()}')
    print(f'size: {stack_obj.capacity()}')
