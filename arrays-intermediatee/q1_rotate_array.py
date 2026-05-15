arr = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter rotations: "))
k = k % len(arr)
print(arr[-k:] + arr[:-k])
