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

"""
Deze functie laad de Postgres DB tabel in. (kan even duren)
"""

def fill_table():
    cur.execute("select * from fav_category")
    fav_category = cur.fetchall()
    if fav_category == []:
        cur.execute("""select l.profid, l.prodid, pr.segment, r.name, r.category, r.subcategory, r.subsubcategory, r.targetaudience
        from profiles_previously_viewed as L inner join profiles as Pr on l.profid = pr.id
        inner join products as r on l.prodid = r.id
        where segment = 'buyer' or segment = 'BUYER'
        order by profid desc,
        prodid desc
        """)
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

def recommend(): # werkt alleen bij profielen waar geen "'s" in de category of targetaudience zit. en als category/targetaudience niet 'null' is.
    fill_table()
    profid = input("Voer een profiel id in:")
    cur.execute("select category, targetaudience from fav_category where profid='{}'".format(profid))
    category = cur.fetchall()
    cur.execute("select id from products where category='{}' and targetaudience='{}'".format(category[0][0], category[0][1]))
    mogelijke_aanbevelingen = cur.fetchall()
    aanbeveling = random.choice(mogelijke_aanbevelingen)
    print("het aanbevolen product voor profiel: {} is {}".format(profid, aanbeveling[0]))

#create_fav_category()
recommend()


