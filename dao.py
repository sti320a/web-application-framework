import os
import sqlite3
import sys
import const
import pprint

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


def signUp(email_confirm_pass):
    if isProvisionalUser(email_confirm_pass) == False:
        return False
    user_info = getUserInfoFromProvisionalUserDb(email_confirm_pass)
    insertUser2Db(user_info["name"], user_info["email"], user_info["auth_key"], db_file_name)
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
def getProvisionalUserList():
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

def getUserList():
    createProvisionalUserTableIfNotExist(db_file_name)
    sql_result = selectReturn("SELECT id, name, email FROM user", db_file_name, True)

    user_list = [] 
    for row in sql_result:
        user_info = {}
        user_info["id"] = row[0]
        user_info["name"] = row[1]
        user_info["email"] = row[2]        
        user_list.append(user_info)

    return user_list

"""
from Provisonal User to User
"""

def isProvisionalUser(email_confirm_pass):
    createProvisionalUserTableIfNotExist(db_file_name)
    sql_result = selectReturn("SELECT id FROM provisionalUser WHERE email_confirm_pass='{}'".format(email_confirm_pass), db_file_name, False)
    user_list = [] 
    for row in sql_result:
        user_list.append(row)

    if len(user_list) <= 0 :
        return False
    return True

def getUserInfoFromProvisionalUserDb(email_confirm_pass):
    createProvisionalUserTableIfNotExist(db_file_name)
    sql_result = selectReturn("SELECT id, name, email, auth_key FROM provisionalUser WHERE email_confirm_pass='{}'".format(email_confirm_pass), db_file_name, False)
    temp_list = [] 
    for row in sql_result:
        temp_list.append(row)

    user_info = {}
    user_info["id"] = temp_list[0][0]
    user_info["name"] = temp_list[0][1]
    user_info["email"] = temp_list[0][2]
    user_info["auth_key"] = temp_list[0][3]

    return user_info

"""
Login and Check User Existing
"""

def isUser(email, auth_key):
    createUserTableIfNotExist(db_file_name)
    sql_result = selectReturn("SELECT id FROM user WHERE email='{}' AND auth_key='{}'".format(email, auth_key), db_file_name, False)
    user_list = [] 
    for row in sql_result:
        user_list.append(row)
    if len(user_list) <= 0 :
        return False
    return True

def getUserInfo(email, auth_key):
    createUserTableIfNotExist(db_file_name)
    sql_result = selectReturn("SELECT id, name, email, auth_key FROM user WHERE email='{}' AND auth_key='{}'".format(email, auth_key), db_file_name, False)
    temp_list = [] 
    for row in sql_result:
        temp_list.append(row)


        user_info = {}
    user_info["id"] = temp_list[0][0]
    user_info["name"] = temp_list[0][1]
    user_info["email"] = temp_list[0][2]
    user_info["auth_key"] = temp_list[0][3]

    #print(user_info)
    return user_info


"""
Save user's post
"""

def insertMovie(userid, title, comment, path):
    
    create("CREATE TABLE IF NOT EXISTS movie (id int, userid int, title varchar(64), comment varchar(2000), path varchar(200), created_at timestamp default (DATETIME('now', 'localtime')), updated_at timestamp default (DATETIME('now', 'localtime')))", "movie")
    id = getNewId4Insert("movie", "movie")
    insert("INSERT INTO movie(id, userid, title, comment, path) VALUES(?,?,?,?,?)", [id,userid,title,comment,path], "movie")

    return True

def getAllMovies():
    
    create("CREATE TABLE IF NOT EXISTS movie (id int, userid int, title varchar(64), comment varchar(2000), path varchar(200), created_at timestamp default (DATETIME('now', 'localtime')), updated_at timestamp default (DATETIME('now', 'localtime')))", "movie")
    sql_result = select("SELECT * FROM movie", "movie", True) 

    temp_list = [] 
    for row in sql_result:
        temp_list.append(row)

    post_list = []
    for row in temp_list:
        post = {}    
        post["id"] = row[0]
        post["userid"] = row[1]
        post["title"] = row[2]
        post["comment"] = row[3]
        post["path"] = row[4]
        post["created_at"] = row[5]
        post["updated_at"] = row[6]
        post_list.append(post)

    return post_list