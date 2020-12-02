from pymongo import MongoClient
import psycopg2


def psycopg_connect():
    conn = psycopg2.connect('dbname=postgres user=postgres password=groep5')
    cur = conn.cursor()
    return conn, cur


def mongo_connect():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.huwebshop
    col = db.products
    ses = db.sessions
    pro = db.profiles
    products = col.find({})
    sessions = ses.find({})
    profiles = pro.find({})
    return products, sessions, profiles