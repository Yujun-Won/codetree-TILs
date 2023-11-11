def is_prime(num):              # 소수 판별 함수
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

# a이상 b이하 수 중 소수 & 모든 자릿수 합이 짝수
def judge_num(a, b):
    cnt = 0
    for i in range(a, b+1):
        if is_prime(i):         # 소수일 경우
            # 1. 한 자리 수
            if len(str(i)) == 1 and i % 2 == 0:
                cnt += 1
            # 2. 두 자리 수
            elif len(str(i)) == 2 and (i // 10 + i % 10) % 2 == 0:
                cnt += 1
    
    return cnt


a, b = map(int, input().split())
print(judge_num(a, b))