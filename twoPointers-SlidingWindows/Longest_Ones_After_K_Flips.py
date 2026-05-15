arr = list(map(int, input("Enter binary array: ").split()))
k = int(input("Enter k: "))

left = 0
zeros = 0
maximum = 0

for right in range(len(arr)):
    if arr[right] == 0:
        zeros += 1

    while zeros > k:
        if arr[left] == 0:
            zeros -= 1
        left += 1

    maximum = max(maximum, right - left + 1)

print(maximum)
