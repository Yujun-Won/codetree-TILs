def is_even_and_5(n):
    return n % 2 == 0 and (n // 10 + (n % 10)) % 5 == 0


n = int(input())

print("Yes" if is_even_and_5(n) else "No")