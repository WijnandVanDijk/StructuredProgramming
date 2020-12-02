from Connections import psycopg_connect
conn, cur=psycopg_connect()

print("Opened database successfully")

cur.execute("DROP TABLE IF EXISTS order_table ")
cur.execute("DROP TABLE IF EXISTS products ")
cur.execute("DROP TABLE IF EXISTS brand ")
cur.execute("DROP TABLE IF EXISTS category ")
cur.execute("DROP TABLE IF EXISTS sub_category ")
cur.execute("DROP TABLE IF EXISTS sub_sub_category ")
cur.execute("DROP TABLE IF EXISTS sessions ")
cur.execute("DROP TABLE IF EXISTS profiles ")



cur.execute("""create table products
            (product_id varchar PRIMARY KEY,
	        brand varchar,
	        category varchar,
	        sub_category varchar,
	        sub_sub_category varchar,
	        gender varchar,
	        target_audience varchar, 
	        price decimal(6,2));""")
cur.execute("""create table sessions
           (session_id varchar PRIMARY KEY           );""")
cur.execute("""CREATE TABLE order_table
           (order_id serial primary key,
           product_id varchar,
           session_id varchar,
           foreign key(product_id) references products(product_id),
           foreign key(session_id) references sessions(session_id));""")
cur.execute("""CREATE TABLE profiles(
            profile_id integer unique primary key 
            )""")





print("New database added")
conn.commit()
cur.close()
conn.close()