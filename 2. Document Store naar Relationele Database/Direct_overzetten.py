from Connections import psycopg_connect
from Connections import mongo_connect

conn,cur=psycopg_connect()
products, sessions, profiles = mongo_connect()


def overzetten_products():
    'Direct overzetten van producten. Kan alleen als de table leeg is.'
    c=0
    for product in products:
        try:
            productid = product['_id']
            brand = product['brand']
            category = product['category']
            sub_category = product['sub_category']
            sub_sub_category = product['sub_sub_category']
            gender = product['gender']

            target_audience = product['properties']['doelgroep']
            price = product['price']['selling_price']
            price = price / 100
            cur.execute("insert into products (product_id, brand, category,sub_category,sub_sub_category, gender,target_audience,price) values (%s,%s,%s,%s,%s,%s,%s,%s)",(productid, brand, category,sub_category,sub_sub_category, gender,target_audience,price))
        except KeyError:
            continue
        c+=1
        if c==1000:
            break
    conn.commit()
    cur.close()
    conn.close()
    return

def overzetten_sessions():
    'Direct overzetten van sessions. Kan alleen als de table leeg is.'
    c=0
    for session in sessions:
        try:
            sessionid = session["_id"]

            cur.execute("insert into products (session_id) values (%s)",(sessionid))
        except KeyError:
            continue
        c+=1
        if c==1000:
            break
    conn.commit()
    cur.close()
    conn.close()
    return



overzetten_products()
overzetten_sessions()