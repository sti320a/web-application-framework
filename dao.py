import os
import sqlite3
import sys
import const

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

db_file_name = const.DB_FILE_NAME

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
    sql_result = c.execute(statement)
    conn.commit()
    result = []
    for row in sql_result:
        result.append(row)
    if(console):
        for row in sql_result:
            print("dao.select:"+row)
    conn.close()
    return result
    

def selectReturn(statement, db_file_name, console):
    conn = sqlite3.connect(ROOT_DIR+'/db/{}.db'.format(db_file_name))
    c = conn.cursor()
    sql_result = c.execute(statement)
    conn.commit()

    result = []
    for row in sql_result:
        result.append(row)
        if(console):print("dao.selectReturn:" + str(row))
    conn.close()

    return result


"""
Practical SQL Function
"""
def getNewId4Insert(table_name, db_file_name):
    userList = selectReturn("SELECT * FROM {}".format(table_name), db_file_name, False);
    if len(userList) == 0:
        return 1
    new_user_id = userList[-1][0] + 1
    if new_user_id==None:
        return False        
    return new_user_id

"""
create user table
"""
def createProvisionalUserTableIfNotExist(db_file_name):
    create("CREATE TABLE IF NOT EXISTS provisionalUser (id int primary key, name varchar(64), email varchar(64), auth_key varchar(64), email_confirm_pass varchar(64))", db_file_name)

def createUserTableIfNotExist(db_file_name):
    create("CREATE TABLE IF NOT EXISTS user (id int primary key, name varchar(64), email varchar(64), auth_key varchar(64), email_confirm_pass varchar(64))", db_file_name)

"""
Provisionally User Sign up  
"""
def insertProvisionalUser2Db(username, email, auth_key, email_confirm_pass, db_file_name):
    createProvisionalUserTableIfNotExist(db_file_name)
    id = getNewId4Insert("provisionalUser",db_file_name)
    insert("INSERT INTO provisionalUser (id, name, email, auth_key, email_confirm_pass) VALUES (?,?,?,?,?)", [id, username, email, auth_key, email_confirm_pass], db_file_name)
    return True

def deleteProvisionalUser2Db(username, email, db_file_name):
    createProvisionalUserTableIfNotExist(db_file_name)
    delete("DELETE FROM provisionalUser WHERE name=? AND email = ?", [username, email], db_file_name)
    return True

"""
User Sign up
"""
def insertUser2Db(username, email, auth_key, db_file_name):
    createUserTableIfNotExist(db_file_name)
    id = getNewId4Insert("user", db_file_name)
    insert("INSERT INTO user (id, name, email, auth_key) VALUES (?,?,?,?)", [id, username, email, auth_key], db_file_name)
    return True

"""
Delete user
"""
def deleteUserFromDb(username, email, auth_key, db_file_name):
    createUserTableIfNotExist(db_file_name)
    delete("DELETE FROM user WHERE name=? AND email=? AND auth_key=?", [username, email, auth_key], db_file_name)
    return True

"""
Account Admin Show User List
"""
def getUserList():
    createProvisionalUserTableIfNotExist(db_file_name)
    sql_result = selectReturn("SELECT id, name, email FROM provisionalUser", db_file_name, True)

    user_list = [] 
    for row in sql_result:
        user_info = {}
        user_info["id"] = row[0]
        user_info["name"] = row[1]
        user_info["email"] = row[2]        
        user_list.append(user_info)

    return user_list