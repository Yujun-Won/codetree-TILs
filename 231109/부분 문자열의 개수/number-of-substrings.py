A = input()
B = input()

cnt = 0

for i in range(len(A)-1):
    if B == A[i:i+len(B)]:
        cnt += 1

print(cnt)