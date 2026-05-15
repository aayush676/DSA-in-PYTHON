arr = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])
