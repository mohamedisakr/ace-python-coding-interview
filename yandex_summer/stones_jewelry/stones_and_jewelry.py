j = input().strip()
s = input().strip()

res = 0
for char in s:
    if char in j:
        res += 1
print(res)
