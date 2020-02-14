zwart = 0
wit = 0
def geeffeedback(zwart, wit):
    code = input('Geef de code: ')
    gok = ('a', 'f', 'd', 'b')
    for i in range(len(code)):
        if gok[i] == code[i]:
            zwart += 1

    for i in range(len(code)):
        if gok[i] != code[i] and gok[i] in code:
            wit += 1

    feedback = [zwart, wit]
    print(feedback)
