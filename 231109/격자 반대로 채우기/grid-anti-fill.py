dx, dy = [0, -1, 0], [-1, 0, 1]         # 북, 서, 남 순서대로

n = int(input())
grid = [[0 for _ in range(n)] for _ in range(n)]

cnt = 1
for j in range(n-1, -1, -1):
    if j % 2 != 0:
        for i in range(n-1, -1, -1):
            grid[i][j] = cnt
            cnt += 1
    else:
        for i in range(n):
            grid[i][j] = cnt
            cnt += 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()