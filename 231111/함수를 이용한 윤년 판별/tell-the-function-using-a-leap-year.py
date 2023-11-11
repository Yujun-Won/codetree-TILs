def is_leapyear(yyyy):
    if yyyy % 4 == 0:
        return True
    if yyyy % 4 == 0 and yyyy % 100 == 0:
        return False
    if yyyy % 4 == 0 and yyyy % 100 == 0 and yyyy % 400 == 0:
        return True
    else:
        return False


yyyy = int(input())

print("true" if is_leapyear(yyyy) else "false")