n = int(input())

if n == 1:
    print('*\n*')
else:
    print('* ' * n)
    print('* ')
    for i in range(1, n-1):
        print('* ' * (n - i))
    for i in range(1, n-1):
        print('* ' * (i + 1))
    print('* ')
    print('* ' * n)