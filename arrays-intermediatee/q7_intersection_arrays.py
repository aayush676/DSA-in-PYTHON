arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

result = []

for i in arr1:
    if i in arr2 and i not in result:
        result.append(i)

print(result)
