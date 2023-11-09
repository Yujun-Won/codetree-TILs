string = input()

target = string[1]
result = ''

for st in string:
    if st == target:
        result += string[0]
    else:
        result += st

print(result)