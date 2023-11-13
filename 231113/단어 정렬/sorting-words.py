n = int(input())

words = [input() for _ in range(n)]
words = sorted(words)

for word in words:
    print(word)