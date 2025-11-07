def weird(num: int) -> None:
    sequence = []
    while num != 1:
        sequence.append(num)
        num = num // 2 if num % 2 == 0 else num * 3 + 1
    sequence.append(1)
    print(" ".join(map(str, sequence)))
