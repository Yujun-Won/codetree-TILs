m1, d1, m2, d2 = map(int, input().split())
day_of_week = input()

#                     1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
days_of_months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = 0

# 1. m1월의 잔여 일수 카운트
count += (days_of_months[m1] - d1 + 1)

# 2. m2월 일수 카운트
count += d2

# 3. (m1 + 1)월부터 (m2 - 1)월까지의 일수 카운트
month_count = m2 - m1 - 1
for i in range(m1+1, m2):
    count += days_of_months[i]

print(count // 7 + 1)