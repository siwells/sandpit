import sqlite3
from sqlite3 import Error

import json

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


def init(conn):
    try:
        cur = conn.cursor()
        cur.execute('create table names (namedocs JSON);')
    except Error as e:
        print(e)


def add_doc(conn, doc):
    try:
        cur = conn.cursor()
        cur.execute("insert into names (namedocs) values (json('"+json.dumps(doc)+"'));")
        conn.commit()
    except Error as e:
        print(e)


def query_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM names")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)


def main():
    database = "test.db"
    jsondoc1 = {'first':'simon', 'last':'wells'}
    jsondoc2 = {'first':'thomas', 'last':'wells'}
 
    conn = create_connection(database)
    init(conn)
    with conn:
        add_doc(conn, jsondoc1)
        query_all(conn)
 
    conn.close()
 
if __name__ == '__main__':
    main()

