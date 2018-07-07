import dao

def signUpUserProvisonally(username, email, password):
    # TODO1 validation check
    if validationCheck4InsertProvisionalUser(username, email, password) == False:
        print("validation error")
        return False

    # TODO2 password to hash

    dao.create("CREATE TABLE IF NOT EXISTS provisionalUser (id int, name varchar(64), email varchar(64), auth_key varchar(64))", "user.db")
    id = getNewUserId4InsertProvisionalUser()
    dao.insert("INSERT INTO provisionalUser (id, name, email, auth_key) VALUES (?,?,?,?)", [id, username, email, password], "user.db")
    dao.select("SELECT * FROM provisionalUser", "user.db", True)

def getNewUserId4InsertProvisionalUser():
    userList = dao.selectReturn("SELECT * FROM provisionalUser", "user.db", True);
    newUserId = userList[-1][0] + 1
    if newUserId==None:
        return False        
    print(newUserId)
    return newUserId

def validationCheck4InsertProvisionalUser(username, email, password):
    if len(password) <= 8:
        print("Password is too short")
        return False
