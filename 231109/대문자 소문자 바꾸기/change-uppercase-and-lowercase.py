string = input()

result = ''

for st in string:
    if st.isupper():
        result += st.lower()
    else:
        result += st.upper()

print(result)