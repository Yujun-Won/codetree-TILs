# 각 문자열에서 알파벳을 제외하고 남은 숫자부분을 차례대로 이어붙여 만든 수
# 두 문자열에서 구한 두 수의 합

string1 = input()
string2 = input()

num1 = ''.join([st for st in string1 if st.isnumeric()])
num2 = ''.join([st for st in string2 if st.isnumeric()])

print(int(num1) + int(num2))