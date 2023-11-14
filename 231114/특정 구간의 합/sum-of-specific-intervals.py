n, m = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(m):
    a1, a2 = map(int, input().split())
    print(sum([A[i-1] for i in range(a1, a2+1)]))