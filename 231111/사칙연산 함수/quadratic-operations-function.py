def add(n,m):
    return n + m

def minus(n,m):
    return n - m

def multiply(n,m):
    return n * m

def divide(n,m):
    return n // m

def branch(n, m, o):
    n, m = int(n), int(m)

    if o == '+':
        return add(n, m)
    elif o == '-':
        return minus(n, m)
    elif o == '*':
        return multiply(n, m)
    elif o == '/':
        return divide(n, m)
    else:
        return False


a, o, c = input().split()

print(f"{a} {o} {c} = {branch(a, c, o)}" if o in ('+', '-', '*', '/') else False)