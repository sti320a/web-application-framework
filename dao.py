import sqlite3
import sys, os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def create():
    conn = sqlite3.connect(ROOT_DIR+'/db/user.db')
    c = conn.cursor()
    create_table="CREATE TABLE IF NOT EXISTS user (id int, name varchar(64))"
    c.execute(create_table)
    conn.commit()
    conn.close()

def insert(id, name):
    conn = sqlite3.connect(ROOT_DIR+'/db/user.db')
    c = conn.cursor()
    insert = "INSERT INTO user(id, name) VALUES(?, ?)"
    place_holder = [id, name]
    c.execute(insert, place_holder)
    conn.commit()
    conn.close()

def selectAll():
    conn = sqlite3.connect(ROOT_DIR+'/db/user.db')
    c = conn.cursor()
    select = "SELECT * FROM user"
    result = c.execute(select)
    conn.commit()
    for row in result:
        print(row)
    conn.close()
    
