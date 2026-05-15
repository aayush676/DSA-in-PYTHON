arr = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

window_sum = sum(arr[:k])
maximum = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]
    maximum = max(maximum, window_sum)

print(maximum)
