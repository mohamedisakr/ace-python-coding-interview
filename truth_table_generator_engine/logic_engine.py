from re import findall


class LogicEngine:
    def __init__(self):
        # We add 'prec' (Precedence) to each gate
        # Higher number = higher priority
        self.GATES = {
            'NOT': {'func': lambda a: not a,      'arity': 1, 'prec': 3},
            'AND': {'func': lambda a, b: a and b, 'arity': 2, 'prec': 2},
            'OR':  {'func': lambda a, b: a or b,  'arity': 2, 'prec': 1},
            'XOR': {'func': lambda a, b: a != b,  'arity': 2, 'prec': 1},
        }
        self.variables = set()
        self.tokens = []

    def tokenize(self, expression):
        # 1. Regex to split string into parts
        raw_tokens = findall(r'\w+|[()&|!^]', expression)
        self.tokens = [t.upper() for t in raw_tokens]

        # 2. Identify variables vs operators
        self.variables.clear()
        categorized = []

        for t in self.tokens:
            if t in self.GATES:
                categorized.append(("OPERATOR", t))
            elif t in "()":
                categorized.append(("PAREN", t))
            else:
                # If it's not a gate or paren, it's a variable
                self.variables.add(t)
                categorized.append(("VARIABLE", t))

        return categorized


# --- Testing the Class ---
engine = LogicEngine()
expression = "(A AND B) OR NOT C"
structured_tokens = engine.tokenize(expression)

print(f"Variables found: {sorted(list(engine.variables))}")
print("Token Stream:")
for kind, value in structured_tokens:
    print(f"  {kind:10} : {value}")
