class MyStack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self) -> bool:
        return len(self.stack_list) == 0

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        self.stack_list.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def capacity(self) -> int:
        return len(self.stack_list)


if __name__ == "__main__":
    stack_obj = MyStack()
    print(f'is_empty: {stack_obj.is_empty()}')
    print(f'peek: {stack_obj.peek()}')
    print(f'size: {stack_obj.capacity()}')
