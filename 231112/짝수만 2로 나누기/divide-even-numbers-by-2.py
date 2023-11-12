n = int(input())
numbers = list(map(int, input().split()))

numbers = [num // 2 if num % 2 == 0 else num for num in numbers]

for num in numbers:
    print(num, end=' ')
print()