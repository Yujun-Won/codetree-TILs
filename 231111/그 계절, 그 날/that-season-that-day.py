# 윤년을 판단하는 함수
def is_leapyear(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    if y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return True
    return False

# 날짜가 존재하는지 판단하는 함수
def is_exist(y, m, d):
    # 1. 30일 또는 31일까지 있는 월
    if m in (1, 3, 5, 7, 8, 10, 12):
        day_limit = 31
    elif m in (4, 6, 9, 11):
        day_limit = 30
    
    # 2. 2월의 경우 (윤년 True or False)
    if m == 2:
        if is_leapyear(y):
            day_limit = 29
        else:
            day_limit = 28

    if d > day_limit:
        return False

    return True

# 최종적으로 계절을 판단하는 함수
def find_season(m):
    if 3 <= m <= 5:
        return "Spring"
    elif 6 <= m <= 8:
        return "Summer"
    elif 9 <= m <= 11:
        return "Fall"
    elif m in (12, 1, 2):
        return "Winter"


y, m, d = map(int, input().split())

print(find_season(m) if is_exist(y, m, d) else -1)