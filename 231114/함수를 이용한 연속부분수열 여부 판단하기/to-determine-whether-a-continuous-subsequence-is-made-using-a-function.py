# n번째 인덱스부터 시작하는 n2길이의 a수열과 b수열이 완전히 일치하는지 확인
def is_same(n):
    for i in range(n2):
        if a[i + n] != b[i]:
            return False

    return True


# b가 a의 연속부분수열인지 확인합니다.
def is_subsequence(n1, n2):
    for i in range(n1 - n2 + 1):
        if is_same(i):
            return True
    
    return False


n1, n2 = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print("Yes" if is_subsequence(n1, n2) else "No")