import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\..\\')
import dao
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

test_user_db = "testUserDb"

os.remove(ROOT_DIR+'/../db/{}.db'.format(test_user_db))

print("Checking creating test user db...")
assert(dao.create("CREATE TABLE IF NOT EXISTS user (id int, name varchar(64))", test_user_db) == True)
assert(len(dao.select("SELECT * FROM user", test_user_db, False)) == 0)

print("Checking insert test user db...")
assert(dao.insert("INSERT INTO user(id, name) VALUES(?,?)", [123, "taro"], test_user_db) == True)
assert(len(dao.select("SELECT * FROM user", test_user_db, False)) == 1)


print("Checking update test user db...")
assert(dao.update("UPDATE user SET name=? WHERE id=?", ["goro", 123], test_user_db) == True)
assert(len(dao.select("SELECT * FROM user", test_user_db, False)) == 1)
assert(dao.select("SELECT * FROM user", test_user_db, False)[0][1] == "goro")


print("Checking delete a column test user db...")
assert(dao.delete("DELETE FROM user WHERE id=?", [123], test_user_db) == True)
assert(len(dao.select("SELECT * FROM user", test_user_db, False)) == 0)


print("Checking insert insert user provisionally into test user db...")
assert(dao.insertProvisionalUser2Db("test:insertProvisionalUser2Db", "email@test.com", "123abc456def", test_user_db) == True)
assert(len(dao.select("SELECT * FROM provisionalUser", test_user_db, False)) == 1)
assert(dao.select("SELECT * FROM provisionalUser", test_user_db, False)[0][1] == "test:insertProvisionalUser2Db")
assert(dao.deleteAll("provisionalUser", test_user_db) == True)
assert(len(dao.select("SELECT * FROM provisionalUser", test_user_db, False)) == 0)


print("Finish All Test.")