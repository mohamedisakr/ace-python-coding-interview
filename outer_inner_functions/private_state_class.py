class Counter:
    def __init__(self):
        # This is the 'state' variable
        self._count = 0

    def increment(self):
        self._count += 1
        return self._count


# Usage
counter = Counter()
counter._count += 1
print(counter.increment())  # 1
print(counter.increment())  # 2
