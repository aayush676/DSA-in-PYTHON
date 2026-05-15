arr = list(map(int, input("Enter numbers: ").split()))
count = 0
for i in arr:
    if i % 2 == 0:
        count += 1
print(count)
