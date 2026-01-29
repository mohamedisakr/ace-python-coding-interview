def create_counter():
    count = 0  # Private state

    def increment():
        nonlocal count
        count += 1
        return count

    return {"inc": increment}


counter = create_counter()
print(counter["inc"]())  # 1
print(counter["inc"]())  # 2
