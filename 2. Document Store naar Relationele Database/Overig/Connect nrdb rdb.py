from pymongo import MongoClient
import psycopg2
import csv


def cursor_created(database_name, user, password):
    # connect met niet-relationele database
    data = "dbname={} user={} password={}".format(database_name, user, password)
    conn = psycopg2.connect(data)
    cur = conn.cursor()
    return cur


def connect_collection(mongo_db, collection_chosen):
    # Connect met een collectie die je kan kiezen bij aanroepen.(procedureel)
    client = MongoClient('mongodb://localhost:27017/')
    database = client[mongo_db]
    collection = database[collection_chosen]  # verbonden met een collectie
    return collection


def create_collection_list(mongo_db, collection_chosen):
    collection_created = connect_collection(mongo_db, collection_chosen).find({})
    return collection_created


cursor_created('AAIrdb', 'postgres', 'postgrespass')  # bij jullie moet het ('postgres', 'postgres', 'groep5') zijn
mongo_db = 'AAIMongo',  # bij jullie moet het denk ik 'huwebshop' zijn.
collection_p, collection_s, collection_pf = 'products', 'sessions', 'profiles'

'''Het volgende is iets omslachtiger dan ik had gewild, maar ik wil niet overdrijven en hier teveel tijd in steken.'''
products = create_collection_list(mongo_db, collection_p)
sessions = create_collection_list(mongo_db, collection_s)
profiles = create_collection_list(mongo_db, collection_pf)


def overzetten_products(collection_wanted):  # bron: slack info van de les gestuurd door rik boss
    with open('test.csv', 'w', newline='') as csvout:
        fieldnames = ['id', 'brand', 'category', 'gender', 'doelgroep', 'price']
        writer = csv.DictWriter(csvout, fieldnames=fieldnames)
        writer.writeheader()
        c = 0
        for item in collection_wanted:
            try:
                productid = item['_id']
                brand = item['brand']
                category = item['category']
                gender = item['gender']
                doelgroep = item['properties']['doelgroep']
                price = item['price']['selling_price']
                price = price / 100
                writer.writerow({'id': productid,
                                 'brand':brand,
                                 'category': category,
                                 'gender':gender,
                                 'doelgroep': doelgroep,
                                 'price': price
                                 })
            except KeyError:
                continue
            c += 1
            if c % 10000 == 0:
                print("{} product records written...".format(c))
    print("Finished creating the product database contents.")


overzetten_products(products)
# \copy products FROM ‘cpath\to\csv.csv’ DELIMITER ‘,’ CSV HEADER;