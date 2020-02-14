import itertools
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


def mogelijkheden():
    mogelijk = tuple(itertools.product(['a', 'b', 'c', 'd', 'e', 'f'], repeat=4))
    print(mogelijk)
#bron voor mogelijkheden: https://docs.python.org/3/library/itertools.html
