def is_even_and_5(n):
    # 1. n이 짝수
    if n % 2 == 0:
        # 2. 각 자리 숫자의 합이 5의 배수
        a, b = str(n)[0], str(n)[1]
        new_num = int(a) + int(b)

        if new_num % 5 == 0:
            return True
        else:
            return False
    else:
        return False


n = int(input())

print("Yes" if is_even_and_5(n) else "No")