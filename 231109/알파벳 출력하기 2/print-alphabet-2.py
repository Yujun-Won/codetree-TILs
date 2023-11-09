n = int(input())

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

idx = 0

for i in range(n):
    for j in range(n):
        if idx == 26:
            idx = 0
        if i <= j:
            print(alphabet[idx], end=' ')
            idx += 1
        else:
            print(' ', end=' ')
    print()