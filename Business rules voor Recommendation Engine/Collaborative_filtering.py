import psycopg2
import random

con = psycopg2.connect(
    host='Localhost',
    database='postgres4',
    user='postgres',
    password='postgres',
    port=5432) #TODO: edit this.
cur = con.cursor()

"""
Functie voor het aanmaken Postgres DB tabel.
"""

def create_fav_category(): # hoeft maar één keer gedraait te worden,
    # na de eerste keer kan je de aanroep weg halen / uit commenten op line 83.
    cur.execute("DROP TABLE IF EXISTS fav_category")
    cur.execute("""create table fav_category(
                profid varchar unique,
                category varchar,
                targetaudience varchar
                )""")

    con.commit()
    fill_table()

"""
Deze functie laad de Postgres DB tabel in. (kan even duren)
"""

def fill_table(): # vergeet niet de database te refreshen iedere keer als u een ander segment kiest
    cur.execute("select * from fav_category")
    fav_category = cur.fetchall()
    if fav_category == []:
        segment = input('Typ het segment in van de klant. \n'
                        'de mogelijkheden zijn: \n'
                        'SHOPPING_CART, buyer, FUN_SHOPPER, leaver, BUYER, browser, judger, comparator, COMPARER, LEAVER, bouncer, JUDGER, BROWSER, BOUNCER \n'
                        '**LET OP** \nDe segmenten staan op volgorde van klein naar groot, hoe groter het segment hoe langer het duurt om de tabel in te laden.'
                        '\nVergeet ook niet de database te refreshen voor de zekerheid. ')
        print('De tabel wordt gevuld, even geduld aub. (Dit kan een paar minuten duren)')
        cur.execute("""select l.profid, l.prodid, pr.segment, r.name, r.category, r.subcategory, r.subsubcategory, r.targetaudience
        from profiles_previously_viewed as L inner join profiles as Pr on l.profid = pr.id
        inner join products as r on l.prodid = r.id
        where segment = '{}'
        order by profid desc,
        prodid desc
        """.format(segment))
        table = cur.fetchall()
        lijst=[]
        for row in table:
            profid = row[0]
            category = row[4]
            targetaudience = row[7]
            if profid not in lijst and targetaudience is not None:
                cur.execute("insert into fav_category (profid, category, targetaudience ) values (%s,%s,%s)",(profid ,category, targetaudience))
            lijst.append(profid)
        print('De tabel is zojuist gevuld!')
    if fav_category != []:
        print('De tabel is al gevuld!')
    con.commit()

"""
Deze functie kijk in Postgres DB tabel en selecteerd de recommendation.
"""

def recommend(profid):
    cur.execute("select * from fav_category")
    table = cur.fetchall()
    # print(table) testing purpose
    for row in table:
        if profid== row[0]:
            category= row[1]
            targetaudience = row[2]

    cur.execute("select id, category, targetaudience from products")
    prodtable = cur.fetchall()
    # print(prodtable) testing purpose
    for row in prodtable:
        if category==row[1] and (targetaudience==row[2] or targetaudience== None):
            prodid = row[0]

    print("item {} is recommended for profile {}".format(prodid, profid))
    return profid, prodid

create_fav_category()
x = input("Geef een van de profiel id's op uit de 'fav_category' tabel uit de database: ")
recommend(x)