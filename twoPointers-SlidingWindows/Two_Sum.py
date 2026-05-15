nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

left = 0
right = len(nums) - 1

nums.sort()

while left < right:
    current = nums[left] + nums[right]

    if current == target:
        print(nums[left], nums[right])
        break
    elif current < target:
        left += 1
    else:
        right -= 1
