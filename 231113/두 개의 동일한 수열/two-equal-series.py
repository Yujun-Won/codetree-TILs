n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

flag = True
for num in zip(A, B):
    a, b = num
    if a != b:
        flag = False

print("Yes" if flag is True else "No")