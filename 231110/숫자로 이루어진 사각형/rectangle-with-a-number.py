def print_num_rect(n):
    nums = '123456789'
    cnt = 0
    for i in range(n):
        for j in range(n):
            print(nums[cnt], end=' ')
            cnt += 1
            if cnt == 9:
                cnt -= 9
        print()


n = int(input())
print_num_rect(n)