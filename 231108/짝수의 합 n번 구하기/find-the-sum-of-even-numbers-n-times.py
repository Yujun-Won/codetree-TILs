n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    nums = [i for i in range(a, b+1) if i % 2 == 0]
    print(sum(nums))