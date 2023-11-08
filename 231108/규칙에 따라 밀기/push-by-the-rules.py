string = input()
cmd = input()

L, R = cmd.count('L'), cmd.count('R')
total = R - L

if total > 0:
    digits = string[:len(string)-total:]
    string = string[-total::]
    print(string + digits)
elif total < 0:
    digits = string[:-total:]
    string = string[-total::]
    print(string + digits)
else:
    print(string)