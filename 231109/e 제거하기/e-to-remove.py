string = input()

cnt = 0
result = ''

for st in string:
    if st == 'e' and cnt == 0:
        cnt += 1
        continue

    result += st

print(result)