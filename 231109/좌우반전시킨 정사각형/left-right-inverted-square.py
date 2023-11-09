n = int(input())

grid = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        grid[i][j] = (i+1) * (j+1)

for i in range(n):
    for j in range(n-1, -1, -1):
        print(grid[i][j], end=' ')
    print()