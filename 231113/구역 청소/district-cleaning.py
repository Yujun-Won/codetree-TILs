a, b = map(int, input().split())
c, d = map(int, input().split())

areas = [a, b, c, d]

min_val = min(areas)
max_val = max(areas)

print(max_val - min_val)