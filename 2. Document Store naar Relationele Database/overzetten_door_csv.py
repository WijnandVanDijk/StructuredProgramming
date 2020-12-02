import csv
from Connections import psycopg_connect
from Connections import mongo_connect

conn,cur=psycopg_connect()

products, sessions, profiles = mongo_connect()


def overzetten_products(filename):  #bron: slack info van de les gestuurd door rik boss
    """
    al deze functies zetten de gegevens over in een csv bestand. Dit bestand zetten wij dan over via de imoprt van postgres,
    want de command voor het overzetten deed het niet.
    """
    with open(filename, 'w', newline='') as csvout:
        fieldnames = ['id','brand', 'category','sub_category','sub_sub_category', 'gender', 'target_audience','price']
        writer = csv.DictWriter(csvout, fieldnames=fieldnames)
        writer.writeheader()
        c = 0
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
                writer.writerow({'id': productid,
                                 'brand':brand,
                                 'category': category,
                                 'sub_category': sub_category,
                                 'sub_sub_category': sub_sub_category,
                                 'gender':gender,
                                 'target_audience': target_audience,
                                 'price': price
                                 })
            except KeyError:
                continue
            c += 1
            if c % 10000 == 0:
                print("{} product records written...".format(c))    #For testing purpose
                print("Finish test")
                break

    print("Finished creating the product database contents.")
def overzetten_sessions(filename): #bron: slack info van de les gestuurd door rik boss
    with open(filename, 'w', newline='') as csvout:
        fieldnames = ["session_id"]
        writer = csv.DictWriter(csvout, fieldnames=fieldnames)
        writer.writeheader()
        c = 0
        for session in sessions:
            try:
                sessionid = session["_id"]
                writer.writerow({'session_id': sessionid
                                 })
            except KeyError:
                continue
            c += 1
            if c % 10000 == 0:
                print("{} product records written...".format(c))
                break #voor testen

def overzetten_order(filename): #bron: slack info van de les gestuurd door rik boss
    with open(filename, 'w', newline='') as csvout:
        fieldnames = ["session_id",'product_id']
        writer = csv.DictWriter(csvout, fieldnames=fieldnames)
        writer.writeheader()
        c = 0
        for session in sessions:
            try:
                sessionid = session["_id"]
                for i in session['events']['products']:
                    productid = i
                    writer.writerow({'session_id': sessionid,
                                'product_id': productid
                                 })
            except KeyError:
                continue
            c += 1
            if c % 10000 == 0:
                print("{} product records written...".format(c))
                break #voor testen

def overzetten_profiles(filename): #bron: slack info van de les gestuurd door rik boss
    with open(filename, 'w', newline='') as csvout:
        fieldnames = ["profile_id"]
        writer = csv.DictWriter(csvout, fieldnames=fieldnames)
        writer.writeheader()
        c = 0
        for profile in profiles:
            try:
                profile_id = profile["_id"]
                writer.writerow({'profile_id': profile_id
                                 })
            except KeyError:
                continue
            c += 1
            if c % 10000 == 0:
                print("{} product records written...".format(c))
                break #voor testen

# overzetten_products('products.csv')
# overzetten_sessions('sessions.csv')
overzetten_order('order_table.csv')
overzetten_profiles("profile.csv")