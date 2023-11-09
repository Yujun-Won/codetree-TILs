alphabets = 'abcdefghijklmnopqrstuvwxyz'

digit = input()

if digit == 'a':
    print('z')
else:
    print(alphabets[alphabets.index(digit) - 1])