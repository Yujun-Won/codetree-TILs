def func(n):
    if n == 0:
        return a1
    elif n == 1:
        return a2
    else:
        return func(n-1) + 2 * func(n-2)

a1, a2 = map(int, input().split())

for i in range(10):
    print(func(i), end=' ')
print()