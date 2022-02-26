#database : store & collecection of data 
#SQL : structure query language

import sqlite3

def connect(dbname):
    conn = sqlite3.connect(dbname)
    
    connect.execute("CREATE TABLE IF NOT EXIST TAJ_HOTELS (NAME TEXT, DESCRIPTION TEXT, ROOM_DETAILS TEXT, PRICING TEXT, ACTUAL_PRICE)")
    
    print("TABLE CREATED SUCCESFULLY!")
    
    conn.close()
    
    
def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)
    print("Inserted into table: " +str(values))
    insert_sql = ("INSERT INTO TAJ_HOTELS (NAME, DESCRIPTION, ROOM_DETAILS, PRICING, ACTUAL_PRICE) VALUES (?, ?, ?, ?, ?)")
    
    conn.execute(insert_sql, values)
    
    conn.commit()
    conn.close()
    
    
def get_hotel_info(dbname):
    conn = sqlite3.connect(dbname)
    
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM TAJ_HOTELS")
    
    table_data = cur.fetchll()
    
    for record in table_data:
        print(record)
    
        
    conn.close()