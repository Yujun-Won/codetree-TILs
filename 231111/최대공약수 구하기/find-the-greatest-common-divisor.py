n, m = map(int, input().split())

n_divisors = [i for i in range(1, n+1) if n % i == 0]

max_val = 0
for div in n_divisors:
    if m % div == 0 and m > max_val:
        max_val = div

print(max_val)