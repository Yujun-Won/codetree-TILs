def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    else:
        return False


year = int(input())

print("true" if is_leap_year(year) else "false")