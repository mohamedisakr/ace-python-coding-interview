from re import findall
from itertools import product


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

    def evaluate(self, postfix_tokens, var_map):
        stack = []

        for token in postfix_tokens:
            if token in self.GATES:
                # 1. Get the gate metadata
                gate = self.GATES[token]

                # 2. Pop the necessary number of arguments (Arity)
                # Note: Pop order is reversed (Right then Left)
                args = [stack.pop() for _ in range(gate['arity'])]
                args.reverse()

                # 3. Apply the function and push result back
                result = gate['func'](*args)
                stack.append(result)
            else:
                # It's a variable, push its True/False value from the map
                stack.append(var_map[token])

        return stack[0]

    def generate_table(self, expression_str):
        # 1. Prepare the engine
        tokens = self.tokenize(expression_str)
        postfix = self.shunting_yard(tokens)

        # Sort variables alphabetically for a consistent table header
        sorted_vars = sorted(list(self.variables))

        # 2. Print Header
        # Create a format string for equal spacing
        col_width = 5
        header = " | ".join([f"{v:^{col_width}}" for v in sorted_vars])
        header += f" | {expression_str}"
        print(header)
        print("-" * len(header))

        # 3. Generate 2^n combinations
        combinations = product([True, False], repeat=len(sorted_vars))

        for combo in combinations:
            # Map the T/F values to their variable names
            var_map = dict(zip(sorted_vars, combo))

            # Calculate the result
            result = self.evaluate(postfix, var_map)

            # 4. Format the row
            # Convert True/False to 1/0 for a cleaner look
            row_values = [f"{int(v):^{col_width}}" for v in combo]
            row_str = " | ".join(row_values)
            print(f"{row_str} | {int(result)}")


# --- Testing the Class ---
# Setup
engine = LogicEngine()
expression = "(A AND B) OR NOT C"
engine.generate_table(expression)

# tokens = engine.tokenize(expression)
# postfix = engine.shunting_yard(tokens)

# # Simulation: If A=True, B=False, C=True
# current_values = {'A': True, 'B': False, 'C': True}

# # Run the engine
# result = engine.evaluate(postfix, current_values)

# print(f"Expression: {expression}")
# print(f"Postfix:    {postfix}")
# print(f"Input:      {current_values}")
# print(f"Result:     {result}")
