from collections import defaultdict


class Budget:
    def __init__(self):
        self.limits = {}
        self.current_spending = defaultdict(float)

    def set_limit(self, category, amount):
        self.limits[category] = amount

    def check_limits(self):
        for category, limit in self.limits.items():
            current = self.current_spending[category]
            if current > limit:
                print(f"Warning: {category} spending (${
                      current:.2f}) exceeds budget (${limit:.2f})")
