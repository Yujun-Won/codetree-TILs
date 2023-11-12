def calculate(a, b):
    if a < b:
        a *= 2
        b += 25
    else:
        a += 25
        b *= 2
    
    print(a, b)


a, b = map(int, input().split())
calculate(a, b)