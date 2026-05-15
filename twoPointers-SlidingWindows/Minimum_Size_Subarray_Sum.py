arr = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

left = 0
current = 0
minimum = float("inf")

for right in range(len(arr)):
    current += arr[right]

    while current >= target:
        minimum = min(minimum, right - left + 1)
        current -= arr[left]
        left += 1

if minimum == float("inf"):
    print(0)
else:
    print(minimum)
