arr = list(map(int, input("Enter numbers: ").split()))

if arr == sorted(arr):
    print("Sorted")
else:
    print("Not Sorted")
