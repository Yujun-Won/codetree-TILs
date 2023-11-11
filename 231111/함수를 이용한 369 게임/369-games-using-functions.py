def is_magic_number(a, b):
    cnt = 0
    # 1. a이상 b이하 수들 중 3, 6, 9 중에 하나가 들어가 있거나
    for i in range(a, b+1):
        cnt3 = str(i).count('3')
        cnt6 = str(i).count('6')
        cnt9 = str(i).count('9')
        
        # 2. 그 숫자 자체가 3의 배수인 숫자의 개수
        if cnt3 + cnt6 + cnt9 > 0 or i % 3 == 0:
            cnt += 1
    
    return cnt


a, b = map(int, input().split())

print(is_magic_number(a, b))