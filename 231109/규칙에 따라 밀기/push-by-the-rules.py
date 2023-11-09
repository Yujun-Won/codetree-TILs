A = input()
commands = input()

def shift_string(A, direction):
    if direction == 'L':
        return A[1:] + A[0]
    elif direction == 'R':
        return A[-1] + A[:-1]

for command in commands:
    A = shift_string(A, command)

print(A)