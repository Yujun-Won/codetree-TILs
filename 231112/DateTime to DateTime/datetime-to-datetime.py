def count_datetime(a, b, c):
    # a: 일, b: 시, c: 분
    mins = 0

    # 1. 일
    mins += (a - 11) * 1440

    # 2. 시
    if b < 11:
        mins -= b * 60
    else:
        mins += (b - 11) * 60
    
    # 3. 분
    if b < 11:
        mins -= b
    else:
        mins += (b - 11)
    
    return mins + 1


a, b, c = map(int, input().split())
print(count_datetime(a, b, c))