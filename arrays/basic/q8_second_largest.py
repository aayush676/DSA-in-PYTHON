arr = list(map(int, input("Enter numbers: ").split()))
arr = list(set(arr))
arr.sort()
print(arr[-2])
