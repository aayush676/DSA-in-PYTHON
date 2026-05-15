arr = list(map(int, input("Enter numbers: ").split()))

freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1

print(freq)
