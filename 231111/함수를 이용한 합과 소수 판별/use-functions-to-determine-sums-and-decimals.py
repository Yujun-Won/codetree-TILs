def is_prime(num):              # 소수 판별 함수
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# a이상 b이하 수 중 소수 & 모든 자릿수 합이 짝수
def judge_num(a, b):
    cnt = 0
    for i in range(a, b+1):
        print(len(str(i)))
        # if is_prime(i):         # 소수