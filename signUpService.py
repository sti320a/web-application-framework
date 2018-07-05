import dao

def signUpUserProvisonally(username, email, password):
    # TODO1 validation check

    # TODO2 password to hash

    dao.create("CREATE TABLE IF NOT EXISTS provisionalUser (id int, name varchar(64), email varchar(64), auth_key varchar(64))", "user.db")
    dao.insert("INSERT INTO provisionalUser (id, name, email, auth_key) VALUES (?,?,?,?)", [1, username, email, password], "user.db")
    dao.select("SELECT * FROM provisionalUser", "user.db", True)