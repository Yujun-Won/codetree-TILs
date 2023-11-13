n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
for num in numbers:
    print(num, end=' ')
print()

numbers.sort(reverse=True)
for num in numbers:
    print(num, end=' ')
print()