def find_lcm(n, m):
    gcd = 0

    for i in range(1, min(n, m)+1):
        if n % i == 0 and m % i == 0:
            gcd = i

    return n * m // gcd

n, m = map(int, input().split())

print(find_lcm(n, m))