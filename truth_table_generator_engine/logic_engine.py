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

    def shunting_yard(self, categorized_tokens):
        output_queue = []
        operator_stack = []

        for kind, value in categorized_tokens:
            if kind == "VARIABLE":
                # Variables go straight to the output
                output_queue.append(value)

            elif kind == "OPERATOR":
                # While there's an operator on the stack with HIGHER or EQUAL precedence
                # pop it to the output before adding the new one
                while (operator_stack and operator_stack[-1] != '(' and
                       self.GATES[operator_stack[-1]]['prec'] >= self.GATES[value]['prec']):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(value)

            elif value == "(":
                operator_stack.append(value)

            elif value == ")":
                # Pop everything until we find the matching opening parenthesis
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()  # Remove the '('

        # Clean up any remaining operators
        while operator_stack:
            output_queue.append(operator_stack.pop())

        return output_queue


# --- Testing the Class ---
engine = LogicEngine()
expression = "(A AND B) OR NOT C"
structured_tokens = engine.tokenize(expression)

print(f"Variables found: {sorted(list(engine.variables))}")
print("Token Stream:")
for kind, value in structured_tokens:
    print(f"  {kind:10} : {value}")
