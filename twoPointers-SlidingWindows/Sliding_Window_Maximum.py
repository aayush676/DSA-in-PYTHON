arr = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

result = []

for i in range(len(arr) - k + 1):
    result.append(max(arr[i:i + k]))

print(result)
