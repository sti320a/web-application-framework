import sqlite3
import sys, os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


# create("CREATE TABLE IF NOT EXISTS user (id int, name varchar(64))")
def create(statement):
    conn = sqlite3.connect(ROOT_DIR+'/db/user.db')
    c = conn.cursor()
    c.execute(statement)
    conn.commit()
    conn.close()

# insert("INSERT INTO user(id, name) VALUES(?,?)", [123, "taro"])
def insert(statement, place_holder):
    conn = sqlite3.connect(ROOT_DIR+'/db/user.db')
    c = conn.cursor()
    c.execute(statement, place_holder)
    conn.commit()
    conn.close()

# update("UPDATE user SET name=? WHERE id=?", ["goro", 123])
def update(statement, place_holder):
    conn = sqlite3.connect(ROOT_DIR+'/db/user.db')
    c = conn.cursor()
    c.execute(statement, place_holder)
    conn.commit()
    conn.close()

# delete("DELETE FROM user WHERE id=?", [123])
def delete(statement, place_holder):
    conn = sqlite3.connect(ROOT_DIR+'/db/user.db')
    c = conn.cursor()
    c.execute(statement, place_holder)
    conn.commit()
    conn.close()
    
# select("SELECT * FROM user", True) / True: print on console  / False: not print on console
def select(statement, console):
    conn = sqlite3.connect(ROOT_DIR+'/db/user.db')
    c = conn.cursor()
    result = c.execute(statement)
    conn.commit()
    if(console):
        for row in result:
            print(row)
    conn.close()
    
