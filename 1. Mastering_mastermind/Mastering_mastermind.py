import itertools
import math

def welkom():  # start de game, verwijst door naar andere functies
    print("Welkom bij het spel Mastermind! \n"
          "als u klaar bent om te spelen klik typ dan 'R'!")
    ready = input()
    if ready == "r":
        game_mode()
    if ready == "R":
        game_mode()
    if ready != "r":
        quit()
    if ready != "R":
        quit()
        

def game_mode():  # gamemode selecter, 4 of 5 lange code. (voor herkansing)
    print('Kies hier een gamemode: \n'
          'Als u met een code van 4 lang wilt spelen typ dan: "4". \n'
          'Als u met een code van vijf lang wilt spelen typ dan: "5" \n'
          'Als u de tweede optie kiest, heeft u een grotere kans dat de computer het niet raad.')
    select = input()
    if select == '4':
        geef_code_4(deCode)
        algoritme_4()
    if select == '5':
        geef_code_5(deCode)
        algoritme_5()

def geef_code_4(y):  # Hier moet de speler de code invoeren, die de computer gaat proberen te kraken.
    # deze wordt gebruikt als de gebruiker voor de 4 lange code kiest
    print("Geef een code die de computer gaat proberen te kraken. \n"
          "De mogelijke kleuren zijn: blauw, geel, rood, oranje, groen en paars. \n"
          "De code moet bestaan uit vier kleuren met een spatie tussen de kleuren. \n"
          "Gebruik alleen kleine letters.")
    x = input().split(" ")
    for i in range(len(x)):
        y.append(x[i])
    return y

def geef_code_5(y):  # Hier moet de speler de code invoeren, die de computer gaat proberen te kraken.
    # deze wordt gebruikt als de gebruiker voor de 4 lange code kiest
    print("Geef een code die de computer gaat proberen te kraken. \n"
          "De mogelijke kleuren zijn: blauw, geel, rood, oranje, groen en paars. \n"
          "De code moet bestaan uit vijf kleuren met een spatie tussen de kleuren. \n"
          "Gebruik alleen kleine letters.")
    x = input().split(" ")
    for i in range(len(x)):
        y.append(x[i])
    return y

def win_check(y, x):  # kijkt of de code gekraakt is of niet.
    if x == y:
        print("De computer heeft de code gekraakt! Volgende keer beter. :c")
        exit()
    else:
        print("De computer heeft nog niet de code gekraakt! Goed bezig!")

def geef_feedback(y, x):  # deze functie geeft feedback op de code die de computer heeft geprobeerd.
    # wit als de kleur wel in de code zit maar niet op die plek,
    # zwart als de kleur goed is en op de goede plek zit.
    zwart = 0
    wit = 0
    gok = y.copy()
    code = x.copy()

    for i in range(len(x)):
        if gok[i] == code[i]:
            zwart += 1
            code[i] = 0
            gok[i] = 1

    for i in range(len(x)):
        if gok[i] != code[i] and gok[i] in code:
            wit += 1
            code[i] = 0
            gok[i] = 1

    feedback = [zwart, wit]
    return feedback

deCode = []
kleuren = ['blauw', 'geel', 'rood', 'oranje', 'groen', 'paars']
# mogelijkheden = list(itertools.product(['blauw', 'geel', 'rood', 'oranje', 'groen', 'paars'], repeat=4))
# dit ^^ werkte niet door de opbouw van de list die gemaakt werd

def mogelijkheden_4(): # deze functie maakt de mogelijkheden voor de standaard optie van het spel, een code van 4 lang dus
    # 1296 lang.
    mogelijkheden = []

    for i in range(6 ** 4):
        index0 = math.floor(i / (6 ** 3)) % 6
        index1 = math.floor(i / (6 ** 2)) % 6
        index2 = math.floor(i / 6) % 6
        index3 = i % 6

        losse_combos = (
                kleuren[index0] + " " + kleuren[index1] + " " + kleuren[index2] + " " + kleuren[index3]).split(" ")
        mogelijkheden.append([losse_combos])
    return mogelijkheden

def mogelijkheden_5(): # deze functie maakt de mogelijkheden voor de 5 lange code.
    # 7776 lang, er is dus een grotere kans dat de computer het fout heeft
    mogelijkheden = []

    for i in range(6 ** 5):
        index0 = math.floor(i / (6 ** 4)) % 6
        index1 = math.floor(i / (6 ** 3)) % 6
        index2 = math.floor(i / (6 ** 2)) % 6
        index3 = math.floor(i / (6 ** 1)) % 6
        index4 = i % 6

        losse_combos = (
                kleuren[index0] + " " + kleuren[index1] + " " + kleuren[index2] + " " + kleuren[index3] + " " + kleuren[
            index4]).split(" ")
        mogelijkheden.append([losse_combos])
    return mogelijkheden

def moeilijkheid(): # hier kan de speler kiezen hoeveel kansen de computer krijgt om de code te kraken.
    # met minder kansen is de kans kleiner dat de computer het kraakt.
    kansenAI = input("Hoeveel kansen wilt u de AI geven om de code te kraken? "
                     "Met minder kansen is de kans dat de AI het raad kleiner. ")
    print(kansenAI)
    return kansenAI

def algoritme_4(): # 'A Simple Strategy' algoritme uit het artikel van Universiteit Groningen. Voor de 4 lange code.
    kansen_ai = moeilijkheid()
    mogelijk = mogelijkheden_4()
    for i in range(0, int(kansen_ai)):
        gok = mogelijk[0][0]
        print("Computer gok: ", gok)

        win_check(gok, deCode)

        fb = geef_feedback(gok, deCode).copy()
        print(fb)

        for j in range(len(mogelijk)):
            if geef_feedback(mogelijk[j][0], gok) != fb:
                mogelijk[j] = 0

        while 0 in mogelijk:
            mogelijk.remove(0)

    print("De computer heeft de code niet gekraakt! U heeft een goede code gemaakt!")

def algoritme_5(): # 'A Simple Strategy' algoritme uit het artikel van Universiteit Groningen. Voor de 5 lange code.
    kansen_ai = moeilijkheid()
    mogelijk = mogelijkheden_5()
    for i in range(0, int(kansen_ai)):
        gok = mogelijk[0][0]
        print("Computer gok: ", gok)

        win_check(gok, deCode)

        fb = geef_feedback(gok, deCode).copy()
        print(fb)

        for j in range(len(mogelijk)):
            if geef_feedback(mogelijk[j][0], gok) != fb:
                mogelijk[j] = 0

        while 0 in mogelijk:
            mogelijk.remove(0)

    print("De computer heeft de code niet gekraakt! U heeft een goede code gemaakt!")

welkom()