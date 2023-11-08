n = int(input())
nums = list(map(int, input().split()))

result = 100
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        num = abs(nums[i] - nums[j])
        if num < result:
            result = num

print(result)