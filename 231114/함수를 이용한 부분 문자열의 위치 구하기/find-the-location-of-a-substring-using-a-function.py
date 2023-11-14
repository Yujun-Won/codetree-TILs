text = input()
pattern = input()


def is_substr(start_idx):
    n, m = len(text), len(pattern)
    
    # 1. 만약 pattern을 매칭 시키기에 text 문자열 범위를 초과하는 경우
    if start_idx + m - 1 >= n:
        return False

    # 2. text를 순회하며 pattern이 존재하는지 확인
    for j in range(m):
        if text[start_idx + j] != pattern[j]:
            return False

    return True


def find_index():
    n = len(text)
    for i in range(n):
        if is_substr(i):
            return i

    return -1


print(find_index())