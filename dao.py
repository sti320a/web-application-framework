import os
import sqlite3
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

"""
Basic SQL Function
"""

# create("CREATE TABLE IF NOT EXISTS user (id int, name varchar(64))", user)
def create(statement, db_file_name):
    conn = sqlite3.connect(ROOT_DIR+'/db/{}.db'.format(db_file_name))
    c = conn.cursor()
    c.execute(statement)
    conn.commit()
    conn.close()
    return True

# insert("INSERT INTO user(id, name) VALUES(?,?)", [123, "taro"], user)
def insert(statement, place_holder, db_file_name):
    conn = sqlite3.connect(ROOT_DIR+'/db/{}.db'.format(db_file_name))
    c = conn.cursor()
    c.execute(statement, place_holder)
    conn.commit()
    conn.close()
    return True

# update("UPDATE user SET name=? WHERE id=?", ["goro", 123], user)
def update(statement, place_holder, db_file_name):
    conn = sqlite3.connect(ROOT_DIR+'/db/{}.db'.format(db_file_name))
    c = conn.cursor()
    c.execute(statement, place_holder)
    conn.commit()
    conn.close()
    return True

# delete("DELETE FROM user WHERE id=?", [123], user)
def delete(statement, place_holder, db_file_name):
    conn = sqlite3.connect(ROOT_DIR+'/db/{}.db'.format(db_file_name))
    c = conn.cursor()
    c.execute(statement, place_holder)
    conn.commit()
    conn.close()
    return True

# delete("user")
def deleteAll(table_name, db_file_name):
    conn = sqlite3.connect(ROOT_DIR+'/db/{}.db'.format(db_file_name))
    c = conn.cursor()
    c.execute("DELETE FROM {}".format(table_name))
    conn.commit()
    conn.close()
    return True

# select("SELECT * FROM user", user, True) / True: print on console  / False: not print on console
def select(statement, db_file_name, console):
    conn = sqlite3.connect(ROOT_DIR+'/db/{}.db'.format(db_file_name))
    c = conn.cursor()
    sqlResult = c.execute(statement)
    conn.commit()
    result = []
    for row in sqlResult:
        result.append(row)
    if(console):
        for row in sqlResult:
            print(row)
    conn.close()
    return result
    

def selectReturn(statement, db_file_name, console):
    conn = sqlite3.connect(ROOT_DIR+'/db/{}.db'.format(db_file_name))
    c = conn.cursor()
    sqlResult = c.execute(statement)
    conn.commit()

    result = []
    for row in sqlResult:
        result.append(row)
        if(console):print(row)
    conn.close()

    return result


"""
Practical SQL Function
"""
def insertProvisionalUser2Db(username, email, auth_key, db_file_name):
    create("CREATE TABLE IF NOT EXISTS provisionalUser (id int, name varchar(64), email varchar(64), auth_key varchar(64))", db_file_name)
    id = getNewUserId4InsertProvisionalUser(db_file_name)
    insert("INSERT INTO provisionalUser (id, name, email, auth_key) VALUES (?,?,?,?)", [id, username, email, auth_key], db_file_name)
    return True

def getNewUserId4InsertProvisionalUser(db_file_name):
    userList = selectReturn("SELECT * FROM provisionalUser", db_file_name, False);
    if len(userList) == 0:
        return 1
    newUserId = userList[-1][0] + 1
    if newUserId==None:
        return False        
    return newUserId
