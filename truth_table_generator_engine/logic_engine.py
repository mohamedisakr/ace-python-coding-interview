from re import findall
from itertools import product
from csv import writer
from os import makedirs, path


class LogicEngine:
    def __init__(self):
        # We add 'prec' (Precedence) to each gate
        # Higher number = higher priority
        self.GATES = {
            'NOT': {'func': lambda a: not a,      'arity': 1, 'prec': 3},
            'AND': {'func': lambda a, b: a and b, 'arity': 2, 'prec': 2},
            'OR':  {'func': lambda a, b: a or b,  'arity': 2, 'prec': 1},
            'XOR': {'func': lambda a, b: a != b,  'arity': 2, 'prec': 1},
            # precedence to 0 because these are usually evaluated last, after all ANDs and ORs.
            'IMPLIES': {'func': lambda a, b: (not a) or b, 'arity': 2, 'prec': 0},
            'EQUIV':   {'func': lambda a, b: a == b,       'arity': 2, 'prec': 0}
        }
        # 2. The Normalization Map (Synonyms)
        self.SYNONYMS = {
            '&': 'AND', '&&': 'AND',
            '|': 'OR',  '||': 'OR',
            '!': 'NOT', '~': 'NOT',
            '^': 'XOR',
            '->': 'IMPLIES', '=>': 'IMPLIES',
            '<->': 'EQUIV',  '<=>': 'EQUIV'
        }
        self.variables = set()
        self.tokens = []

    def tokenize(self, expression):
        # 1. Regex to split string into parts
        # Updated Regex to handle multi-character symbols like <-> and ->
        raw_tokens = findall(r'<->|->|=>|<=|==|\w+|[()&|!^~]', expression)
        # Updated regex to catch -> and <->
        # raw_tokens = findall(r'<->|->|\w+|[()&|!^]', expression)
        # raw_tokens = findall(r'\w+|[()&|!^]', expression)
        self.tokens = [t.upper() for t in raw_tokens]

        # 2. Identify variables vs operators
        self.variables.clear()
        categorized = []

        for t in raw_tokens:
            t_upper = t.upper()

            # 3. Use the Normalization Map here
            actual_token = self.SYNONYMS.get(t_upper, t_upper)

            if actual_token in self.GATES:
                categorized.append(("OPERATOR", actual_token))
            elif actual_token in "()":
                categorized.append(("PAREN", actual_token))
            else:
                self.variables.add(actual_token)
                categorized.append(("VARIABLE", actual_token))

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

    def evaluate_with_history(self, postfix, var_map):
        stack = []
        history = {}
        for token in postfix:
            if token in self.GATES:
                gate = self.GATES[token]
                args = [stack.pop() for _ in range(gate['arity'])]
                args.reverse()

                vals = [a['val'] for a in args]
                labels = [a['label'] for a in args]

                res_val = gate['func'](*vals)
                # Format label: (A AND B)
                res_label = f"({labels[0]} {token} {labels[1]})" if gate['arity'] == 2 else f"({token} {labels[0]})"

                stack.append({'val': res_val, 'label': res_label})
                history[res_label] = res_val
            else:
                stack.append({'val': var_map[token], 'label': token})
        return stack[0]['val'], history

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

    def export_table(self, expr_str, filename, file_format='markdown'):
        # 1. Logic Processing (same as before)
        tokens = self.tokenize(expr_str)
        postfix = self.shunting_yard(tokens)
        sorted_vars = sorted(list(self.variables))

        dummy_map = {v: True for v in sorted_vars}
        _, history = self.evaluate_with_history(postfix, dummy_map)
        all_cols = sorted_vars + list(history.keys())

        # 2. Prepare Data Rows
        rows = []
        for combo in product([True, False], repeat=len(sorted_vars)):
            v_map = dict(zip(sorted_vars, combo))
            _, hist = self.evaluate_with_history(postfix, v_map)
            row = [int(v_map[v]) for v in sorted_vars] + [int(hist[c])
                                                          for c in all_cols[len(sorted_vars):]]
            rows.append(row)

        # 3. Handle File Directory
        # This ensures the files go into an 'outputs' folder in your project directory
        output_dir = "logic_outputs"
        if not path.exists(output_dir):
            makedirs(output_dir)

        # Combine folder path with filename
        file_path = path.join(output_dir, filename)

        # 4. Write based on format
        if file_format.lower() == 'csv':
            self._write_csv(file_path, all_cols, rows)
        elif file_format.lower() == 'markdown':
            self._write_markdown(file_path, all_cols, rows)

        print(f"File saved to: {path.abspath(file_path)}")

    def _write_csv(self, path, headers, rows):
        with open(path, 'w', newline='', encoding='utf-8') as f:
            the_writer = writer(f)
            the_writer.writerow(headers)
            the_writer.writerows(rows)

    def _write_markdown(self, path, headers, rows):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f"# Truth Table for: {headers[-1]}\n\n")  # Title
            f.write("| " + " | ".join(headers) + " |\n")
            f.write("| " + " | ".join(["---"] * len(headers)) + " |\n")
            for row in rows:
                f.write("| " + " | ".join(map(str, row)) + " |\n")


# --- Final Run ---
engine = LogicEngine()
expression = "(A & B) -> C"

# This will create a folder 'logic_outputs' and put both files inside it
engine.export_table(expression, "results.md", "markdown")
engine.export_table(expression, "results.csv", "csv")

# # --- Final Execution ---
# engine = LogicEngine()
# expr = "(A & B) -> (C <-> A)"

# # Save as a Markdown file
# engine.export_table(expr, "logic_table.md", file_format='markdown')

# # Save as a CSV file for Excel
# engine.export_table(expr, "logic_table.csv", file_format='csv')

# --- Testing the Class ---
# Setup
# engine = LogicEngine()
# # expression = "(A AND B) OR NOT C"
# expression = "(A & B) -> (C <-> A)"
# engine.generate_table(expression)

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
