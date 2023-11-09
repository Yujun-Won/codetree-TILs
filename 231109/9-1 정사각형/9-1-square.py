nums = '987654321'

n = int(input())

idx = 0

for i in range(n):
    for j in range(n):
        print(nums[idx], end='')
        idx += 1
        if idx == len(nums):
            idx = 0
    print()