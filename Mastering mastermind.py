import itertools
import random
zwart = 0
wit = 0
feedback = [zwart, wit]
fb = feedback.copy()

mogelijkheden = list(itertools.product(['a', 'b', 'c', 'd', 'e', 'f'], repeat=4))
# bron voor mogelijkheden: https://docs.python.org/3/library/itertools.html


def random_gok():
    global gok
    gok = random.choice(mogelijkheden)
    print(gok) # print de gok die gedaan is. for testing purposes
    geeffeedback(zwart, wit)


def geef_feedback(zwart, wit):
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

"""
def algoritme1():
    for i in mogelijkheden:
        geeffeedback() # geeft elk item een feedback
    if feedback < fb:
        i = 'q' # als de feedback slechter is dan de eerste gok, krijgt het de waarde 'q'
        mogelijkheden.remove('q') # item wordt verwijderd omdat het een slechtere feedback heeft.

    Het werkt niet, ik heb het hele weekend er aan gewerkt om het werkende te krijgen.
    Maar het is tevergeefs. Ik snap dat als de feedback minder goed is, het item uit de lijst verwijderd moet worden.
    Mijn codering skills laten mij in de steek at the moment, ik werk nog aan mijn programmeer skills.
"""

"""
def algoritme2()
    

"""
randomgok()