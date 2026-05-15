arr = list(map(int, input("Enter numbers: ").split()))

count = 0
candidate = None

for num in arr:
    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1

print(candidate)
