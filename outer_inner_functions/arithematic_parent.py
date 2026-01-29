def arithmetic():
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b != 0:
            return a / b

    return (add, subtract, multiply, divide)


parent = arithmetic()
add = parent[0]
print(type(add))
print(add(10, 20))
