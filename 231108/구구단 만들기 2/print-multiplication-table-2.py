a, b = map(int, input().split())

multipliers = [i for i in range(b, a-1, -1)]
multiplicands = [2, 4, 6, 8]

for i in multiplicands:
    cnt = 0
    for j in multipliers:
        cnt += 1
        if cnt < len(multipliers):
            print(f"{j} * {i} = {j * i}", end=' / ')
        else:
            print(f"{j} * {i} = {j * i}")