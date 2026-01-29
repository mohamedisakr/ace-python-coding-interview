def arithmetic():
    # These inner functions are 'closed' within the factory scope
    def add(a, b): return a + b
    def subtract(a, b): return a - b
    def multiply(a, b): return a * b
    def divide(a, b): return a / b if b != 0 else "Error"

    # Return a mapping rather than a list or tuple
    return {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }


parent = arithmetic()
add = parent["add"]
print(type(add))
print(add(10, 20))
