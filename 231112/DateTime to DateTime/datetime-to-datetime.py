def count_datetime(a, b, c):
    d = a - 11
    h = b - 11
    m = c - 11

    if d == 0 and h == 0 and m == 0:        # 1. 같은 시간
        mins = 0
    elif d == 0 and (h < 0 or m < 0):       # 2. 이전 시간
        mins = -1
    else:
        mins = d * 1440 + h * 60 + m

    print(mins)

a, b, c = map(int, input().split())
count_datetime(a, b, c)