n = int(input('Hoe groot?'))
asterisk = '*'

for i in range(n):
    for j in range(0, i+1):
        print(asterisk, end="")
    print()

for i in range(n):
    for j in range(n-1, i, -1):
        print(asterisk, end="")
    print()
