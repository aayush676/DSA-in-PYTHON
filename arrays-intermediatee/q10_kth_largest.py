arr = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

arr = list(set(arr))
arr.sort(reverse=True)

print(arr[k - 1])
