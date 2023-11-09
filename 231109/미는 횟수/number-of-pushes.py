A = input()
B = input()

def shiftDigit(string):
    return string[-1] + string[:len(string)-1]

cnt = 0
while cnt < len(A):
    A = shiftDigit(A)
    cnt += 1
    if A == B:
        break

print(-1 if cnt == len(A) else cnt)