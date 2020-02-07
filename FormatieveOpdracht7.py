import random

nummer = random.randrange(1, 25)
# print hidden

gok = int(input("Kies een getal van 1 tot 25: "))

if gok == nummer:
    print("JAAAAA! Helemaal goed, goed gedaan")
elif gok < nummer:
    print("Te laag!")
else:
    print("Te hoog!")

# Bron: https://pynative.com/python-random-randrange/

