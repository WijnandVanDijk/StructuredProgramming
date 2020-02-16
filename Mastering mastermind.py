import itertools
import random
zwart = 0
wit = 0

mogelijkheden = list(itertools.product(['a', 'b', 'c', 'd', 'e', 'f'], repeat=4))
# bron voor mogelijkheden: https://docs.python.org/3/library/itertools.html


def randomgok():
    global gok
    gok = random.choice(mogelijkheden)
    print(gok)
    geeffeedback(zwart, wit)


def geeffeedback(zwart, wit):
    code = input('Geef de code: ')
    for i in range(len(code)):
        if gok[i] == code[i]:
            zwart += 1

    for i in range(len(code)):
        if gok[i] != code[i] and gok[i] in code:
            wit += 1

    global feedback
    feedback = [zwart, wit]
    print(feedback)


def gok2():

