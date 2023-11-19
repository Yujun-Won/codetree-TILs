def print_helloworld(n):
    if n == 0:
        return

    print_helloworld(n - 1)
    print("HelloWorld")


n = int(input())

print_helloworld(4)