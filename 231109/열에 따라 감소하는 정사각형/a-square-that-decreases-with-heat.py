n = int(input())

grid = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        grid[i][j] = n - j

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()