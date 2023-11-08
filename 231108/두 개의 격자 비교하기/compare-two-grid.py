n, m = map(int, input().split())

grid1 = [list(map(int, input().split())) for _ in range(n)]
grid2 = [list(map(int, input().split())) for _ in range(n)]

result = []
for i in range(n):
    temp = []
    for j in range(m):
        if grid1[i][j] == grid2[i][j]:
            temp.append(0)
        else:
            temp.append(1)
    result.append(temp)

for i in range(n):
    for j in range(m):
        print(result[i][j], end=' ')
    print()