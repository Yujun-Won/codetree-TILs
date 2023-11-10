def sum_div(n):
    result = sum([i for i in range(1, n+1)])
    return result // 10


n = int(input())
print(sum_div(n))