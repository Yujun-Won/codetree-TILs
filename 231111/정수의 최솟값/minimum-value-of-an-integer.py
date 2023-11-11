def find_min(a, b, c):
    min_val = a
    
    if b < min_val:
        min_val = b
    if c < min_val:
        min_val = c
    
    return min_val


x, y, z = map(int, input().split())

print(find_min(x, y, z))