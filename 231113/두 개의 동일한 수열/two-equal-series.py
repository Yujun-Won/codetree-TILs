n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

flag = True
for a, b in zip(A, B):
    if a != b:
        flag = False

print("Yes" if flag is True else "No")