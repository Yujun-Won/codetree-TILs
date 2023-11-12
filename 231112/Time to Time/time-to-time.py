a, b, c, d = map(int, input().split())

start_time = 60 * a + b
end_time = 60 * c + d

print(end_time - start_time)