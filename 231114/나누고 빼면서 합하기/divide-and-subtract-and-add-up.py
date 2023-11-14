n, m = map(int, input().split())
A = list(map(int, input().split()))

indices = []

# m이 1이 되기 전까지 m이 홀수면 1 빼고, 짝수면 2로 나누기 반복
while m >= 1:
    indices.append(m)

    if m % 2 == 0:      # 짝수면 나누기 2
        m //= 2
    else:               # 홀수면 빼기 1
        m -= 1

result = sum([A[idx - 1] for idx in indices])

print(result)