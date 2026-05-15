arr = list(map(int, input("Enter numbers: ").split()))

result = []

for i in range(len(arr)):
    product = 1

    for j in range(len(arr)):
        if i != j:
            product *= arr[j]

    result.append(product)

print(result)
