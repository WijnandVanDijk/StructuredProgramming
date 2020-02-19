import itertools
import random


mogelijkheden = list(itertools.product(['a', 'b', 'c', 'd', 'e', 'f'], repeat=4))
# bron voor mogelijkheden: https://docs.python.org/3/library/itertools.html
# de computer kiest de code en de speler moet de code raden.


def welkom():
    play = input('Welkom bij mastermind, de computer kiest een code en u moet proberen de code te raden'
          'als u klaar bent om te spelen typ dan "R", als u niet wilt spelen typ dan "C"') # r voor Ready en c voor cancel
    if play.capitalize() == 'R':
        geeffeedback()
    if play.capitalize() == 'C':
        quit()


def geeffeedback():
    code = random.choice(mogelijkheden)
    sets = 0
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
        print(code)
        if feedback != [4, 0]:
            sets += 1
        if feedback == [4, 0]:
            print('Gefeliciteerd je hebt de code gekraakt in,', sets, 'zetten')
            quit()



welkom()