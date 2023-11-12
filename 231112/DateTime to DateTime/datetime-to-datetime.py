# def count_datetime(a, b, c):
a, b, c = map(int, input().split())

d = a - 11
h = b - 11
m = c - 11

mins = d * 1440 + h * 60 + m

if a == 11 and h <= 11 and m <= 11:
    mins = -1



print(mins)
# print(count_datetime(a, b, c))