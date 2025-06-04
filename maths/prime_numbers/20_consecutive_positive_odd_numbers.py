# Q.4 If the sum of the first 20 consecutive positive odd numbers is divided by 202, the
# result is

# (A) 1
# (B) 20
# (C) 2
# (D) 1/2

total = 0
for num in range(1, 41, 2):
    total += num
    print(f'number: {num}')

print(total)
