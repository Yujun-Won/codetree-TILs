n = int(input())

ptr = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if i % 2 != 0:
            ptr += 1
        else:
            ptr += 2
        print(ptr, end=' ')
    print()