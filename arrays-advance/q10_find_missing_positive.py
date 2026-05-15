arr = list(map(int, input("Enter numbers: ").split()))

n = len(arr)

for i in range(n):
    while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
        arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]

for i in range(n):
    if arr[i] != i + 1:
        print(i + 1)
        break
else:
    print(n + 1)
