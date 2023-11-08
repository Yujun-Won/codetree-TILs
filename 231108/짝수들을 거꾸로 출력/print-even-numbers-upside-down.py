n = int(input())
nums = list(map(int, input().split()))

result = [i for i in nums[::-1] if i % 2 == 0]

for res in result:
    print(res, end=' ')
print()