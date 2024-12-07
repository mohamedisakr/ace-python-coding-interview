from collections import Counter


class TwoSum:
    def __init__(self):
        self.counter = Counter()

    def add(self, number: int) -> None:
        self.counter[number] += 1

    def find(self, value: int) -> bool:
        for key, freq in self.counter.items():
            complement = value - key
            if key == complement and freq > 1:
                return True
            if key != complement and complement in self.counter:
                return True

        return False
