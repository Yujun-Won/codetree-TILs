def is_palindrome(string):
    if string == string[::-1]:
        return True
    
    return False


A = input()
print("Yes" if is_palindrome(A) else "No")