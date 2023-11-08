n = int(input())

nums = list(map(int, input().split()))

cnt = 0
idx = 0
for num in nums:
    idx += 1
    if num == 2:
        cnt += 1
        if cnt == 3:
            print(idx)