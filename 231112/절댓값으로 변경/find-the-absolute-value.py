n = int(input())
numbers = list(map(int, input().split()))

numbers = [abs(num) for num in numbers]

for num in numbers:
    print(num, end=' ')
print()