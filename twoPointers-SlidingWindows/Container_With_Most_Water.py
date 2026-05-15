height = list(map(int, input("Enter heights: ").split()))

left = 0
right = len(height) - 1
maximum = 0

while left < right:
    area = min(height[left], height[right]) * (right - left)
    maximum = max(maximum, area)

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(maximum)
