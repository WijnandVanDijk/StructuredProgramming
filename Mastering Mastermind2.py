import itertools
import random


mogelijkheden = list(itertools.product(['a', 'b', 'c', 'd', 'e', 'f'], repeat=4))


def geeffeedback():
    code = random.choice(mogelijkheden)
    for i in range(0,11):
        zwart = 0
        wit = 0
        gok = input('Doe een gok: ')
        for i in range(len(code)):
            if gok[i] == code[i]:
                zwart += 1

        for ii in range(len(code)):
            if gok[ii] != code[ii] and gok[ii] in code:
                wit += 1

        feedback = [zwart, wit]
        print(feedback)

geeffeedback()