def is_more_than_2(string):
    digit_dict = {}

    for digit in A:
        if digit not in digit_dict:     # 없는 것 원소 추가
            digit_dict[digit] = 1
        else:                           # 있는 것 갯수 추가
            digit_dict[digit] += 1

    return True if len(digit_dict) >= 2 else False


A = input()
print("Yes" if is_more_than_2(A) else "No")