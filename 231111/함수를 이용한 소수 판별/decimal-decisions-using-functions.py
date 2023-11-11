def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return n


a, b = map(int, input().split())

total_sum = 0
for i in range(a, b+1):
    if isPrime(i):
        total_sum += i

print(total_sum)