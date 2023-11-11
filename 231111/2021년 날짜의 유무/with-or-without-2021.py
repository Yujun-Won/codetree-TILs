def is_exist(M, D):
    calendar_2021 = {1: 31, 2: 28, 3: 31, 4: 30,
                    5: 31, 6: 30, 7: 30, 8: 31,
                    9: 30, 10: 31, 11: 30, 12: 31}

    if M >= 13 or calendar_2021[M] < D:
        return False
    
    return True


M, D = map(int, input().split())
print("Yes" if is_exist(M, D) else "No")