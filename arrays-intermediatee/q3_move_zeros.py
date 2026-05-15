arr = list(map(int, input("Enter numbers: ").split()))
result = [i for i in arr if i != 0]

zeros = [0] * arr.count(0)

print(result + zeros)
