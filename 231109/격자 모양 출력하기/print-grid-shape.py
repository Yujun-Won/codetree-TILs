n, m = map(int, input().split())

grid = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    grid[x-1][y-1] = x * y

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()