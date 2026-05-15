arr = list(map(int, input("Enter numbers: ").split()))
x = int(input("Enter element to search: "))
if x in arr:
    print("Found")
else:
    print("Not Found")
