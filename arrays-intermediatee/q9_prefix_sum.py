arr = list(map(int, input("Enter numbers: ").split()))

prefix = []
current = 0

for i in arr:
    current += i
    prefix.append(current)

print(prefix)
