import itertools
import random
zwart = 0
wit = 0
feedback = [zwart, wit]
fb = feedback.copy()

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

""""
def algoritme():
    for i in mogelijkheden:
        geeffeedback() # geeft elk item een feedback
    if feedback < fb:
        i = 'q' # als de feedback slechter is dan de eerste gok, krijgt het de waarde 'q'
        mogelijkheden.remove('q') # item wordt verwijderd omdat het een slechtere feedback heeft.

    het werkt niet, ik heb het hele weekend er aan gewerkt om het werkende te krijgen.
    maar het is tevergeefs. ik snap dat als de feedback minder goed is, het item uit de lijst verwijderd moet worden
"""



