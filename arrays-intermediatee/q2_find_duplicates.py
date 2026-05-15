arr = list(map(int, input("Enter numbers: ").split()))
duplicates = []

for i in arr:
    if arr.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)
