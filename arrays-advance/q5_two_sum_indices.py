arr = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

d = {}

for i in range(len(arr)):
    diff = target - arr[i]

    if diff in d:
        print(d[diff], i)
        break

    d[arr[i]] = i
