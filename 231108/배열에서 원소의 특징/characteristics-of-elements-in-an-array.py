nums = list(map(int, input().split()))

for num in nums:
    if num % 3 == 0:
        idx = nums.index(num)
        break

print(nums[idx - 1])