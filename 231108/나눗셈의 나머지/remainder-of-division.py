from collections import Counter

a, b = map(int, input().split())

nums = []
while a > 1:
    nums.append(a % b)
    a //= b

cnts = list(Counter(nums).values())
result = 0

for cnt in cnts:
    result += cnt ** 2

print(result)