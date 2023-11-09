n = int(input())

for i in range(n):
    for j in range(n):
        if i == j:
            print(n, end=' ')
        elif i > j:
            print(n - i + j, end=' ')
    print()