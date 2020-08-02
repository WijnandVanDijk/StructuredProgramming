import psycopg2
import random

con = psycopg2.connect(
    host='Localhost',
    database='postgres2',
    user='postgres',
    password='postgres',
    port=5432)
cur = con.cursor()

"""
Globaal om het sneller te laten lopen.
"""

cur.execute("SELECT id, sellingprice FROM products WHERE sellingprice < 101")
very_cheap = cur.fetchall()

cur.execute("SELECT id, sellingprice FROM products WHERE sellingprice > 100 and sellingprice < 251")
cheap = cur.fetchall()

cur.execute("SELECT id, sellingprice FROM products WHERE sellingprice > 250 and sellingprice < 501")
middle = cur.fetchall()

cur.execute("SELECT id, sellingprice FROM products WHERE sellingprice > 500 and sellingprice < 751")
expensive = cur.fetchall()

cur.execute("SELECT id, sellingprice FROM products WHERE sellingprice > 750")
more_expensive = cur.fetchall()


"""
Functie voor het aanmaken Postgres DB tabel.
"""

def create_prijs_aanbevelingen():
    cur.execute('DROP TABLE IF EXISTS Prijs_aanbevelingen;')
    cur.execute('CREATE TABLE Prijs_aanbevelingen (id varchar PRIMARY KEY,'
                'PRODUCT1 varchar,'
                'PRODUCT2 varchar,'
                'PRODUCT3 varchar,'
                'PRODUCT4 varchar,'
                'PRODUCT5 varchar);')
    con.commit()


"""" 
In deze functie wordt bepaald in welke prijsklasse het product hoort,
en keert daarna 5 random waardes terug uit die prijsklasse.
"""

def prijs(id, prijs_prod):
    if str(prijs_prod) < str(101):
        return [id, random.choice(very_cheap)[0], random.choice(very_cheap)[0], random.choice(very_cheap)[0],
                random.choice(very_cheap)[0], random.choice(very_cheap)[0]]

    elif str(100) < str(prijs_prod) < str(251):
        return [id, random.choice(cheap)[0], random.choice(cheap)[0], random.choice(cheap)[0],
                random.choice(cheap)[0],
                random.choice(cheap)[0]]

    elif str(250) < str(prijs_prod) < str(501):
        return [id, random.choice(middle)[0], random.choice(middle)[0], random.choice(middle)[0],
                random.choice(middle)[0], random.choice(middle)[0]]

    elif str(500) < str(prijs_prod) < str(751):
        return [id, random.choice(expensive)[0], random.choice(expensive)[0], random.choice(expensive)[0],
                random.choice(expensive)[0], random.choice(expensive)[0]]

    elif str(prijs_prod) > str(750):
        return [id, random.choice(more_expensive)[0], random.choice(more_expensive)[0],
                random.choice(more_expensive)[0], random.choice(more_expensive)[0],
                random.choice(more_expensive)[0]]


"""
Deze functie zorgt ervoor dat alle waardes worden ingeladen
Maakt gebruikt van prijs() om te bepalen wat er in komt.
"""

def fill_table():
    create_prijs_aanbevelingen()

    cur.execute("select id,sellingprice from products")
    id_price = cur.fetchall()

    counter = 0

    for id in id_price:
        recids = prijs(id[0], id[1])

        try:
            cur.execute(
                "INSERT INTO Prijs_aanbevelingen (id, PRODUCT1, PRODUCT2, PRODUCT3, PRODUCT4, PRODUCT5) VALUES ( %s, %s, %s, %s,%s,%s)",
                (recids[0], recids[1], recids[2], recids[3], recids[4], recids[5]))
        except:
            print("error", recids)

        counter += 1
        if counter % 1000 == 0:
            print(counter, "/34000 producten zijn ingeladen")

    print("Table filled")

    # Print de gegevens van de data uit, het eerste product is het 'geselecteerde product' en de gevolgde 5 nummers
    # zijn de aanbevolen producten op basis van de prijs van het geselecteerde product
    cur.execute('select id, PRODUCT1, PRODUCT2, PRODUCT3, PRODUCT4, PRODUCT5 from prijs_aanbevelingen')
    x = cur.fetchall()
    print(x)

    con.commit()

def main_loop():
    create_prijs_aanbevelingen()
    fill_table()
    cur.close()

main_loop()

"""
#Als u wilt testen of de gegevens ook echt kloppen, kunt u hier testen of het ook echt zo is.

#('44817', '43811', '31322', '35158', '44263', '39337')
#Dit is een gedeelte van de gegevens die uitgeprint zijn.

cur = con.cursor()

cur.execute("select id, sellingprice from products where id like '44817' ")
test0 = cur.fetchall()

cur.execute("select id, sellingprice from products where id like '43811' ")
test1 = cur.fetchall()

cur.execute("select id, sellingprice from products where id like '31322' ")
test2 = cur.fetchall()

cur.execute("select id, sellingprice from products where id like '35158' ")
test3 = cur.fetchall()

cur.execute("select id, sellingprice from products where id like '44263' ")
test4 = cur.fetchall()

cur.execute("select id, sellingprice from products where id like '39337' ")
test5 = cur.fetchall()

print(test0)
print(test1)
print(test2)
print(test3)
print(test4)
print(test5)

#Als u het zelf wilt testen met een random uitgeprint stukje kunt u dat doen doormiddel van de getallen aan te passen in
# de executes.
"""