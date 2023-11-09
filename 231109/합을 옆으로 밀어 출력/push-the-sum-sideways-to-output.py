n = int(input())

nums = str(sum([int(input()) for _ in range(n)]))

print(nums[1:] + nums[0])