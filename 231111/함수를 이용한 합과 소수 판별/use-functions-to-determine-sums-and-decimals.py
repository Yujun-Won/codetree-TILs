# 소수 판별 함수
def is_prime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

# 자리수의 합 짝수 여부 판단 함수
def is_digit_sum_even(num):
    digit_sum = (num // 100) + ((num // 10) % 10) + (num % 10)
    if digit_sum % 2 == 0:
        return True
    
    return False

# 최종 판단 함수
def judge_num(a, b):
    cnt = 0
    for i in range(a, b+1):
        if is_prime(i) and is_digit_sum_even(i):
            cnt += 1
            
    return cnt


a, b = map(int, input().split())
print(judge_num(a, b))