n = int(input())

grid = [['*' for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 or i == (n-1) or j == 0 or j == (n-1):
            continue
        elif i == j or i < j:
            grid[i][j] = ' '

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()