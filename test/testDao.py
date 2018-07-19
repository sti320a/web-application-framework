import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\..\\')
import dao
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

test_user_db = "testUserDb"

if os.path.exists(ROOT_DIR+'/../db/{}.db'.format(test_user_db)):
    os.remove(ROOT_DIR+'/../db/{}.db'.format(test_user_db))

print("Checking creating test user db...")
assert(dao.create("CREATE TABLE IF NOT EXISTS test(id int, name varchar(64))", test_user_db) == True)
assert(len(dao.select("SELECT * FROM test", test_user_db, False)) == 0)

print("Checking insert test user db...")
assert(dao.insert("INSERT INTO test(id, name) VALUES(?,?)", [123, "taro"], test_user_db) == True)
assert(len(dao.select("SELECT * FROM test", test_user_db, False)) == 1)

print("Checking update test user db...")
assert(dao.update("UPDATE test SET name=? WHERE id=?", ["goro", 123], test_user_db) == True)
assert(len(dao.select("SELECT * FROM test", test_user_db, False)) == 1)
assert(dao.select("SELECT * FROM test", test_user_db, False)[0][1] == "goro")

print("Checking delete a column test test db...")
assert(dao.delete("DELETE FROM test WHERE id=?", [123], test_user_db) == True)
assert(len(dao.select("SELECT * FROM test", test_user_db, False)) == 0)

print("Checking insert user provisionally into test user db...")
assert(dao.insertProvisionalUser2Db("name_test_1", "email@test.com", "123abc456def", "oneTimePassforUserEmailComfirm", test_user_db) == True)
assert(dao.insertProvisionalUser2Db("name_test_2", "email@test.com", "123abc456def", "oneTimePassforUserEmailComfirm2", test_user_db) == True)
assert(len(dao.select("SELECT * FROM provisionalUser", test_user_db, False)) == 2)
assert(dao.select("SELECT * FROM provisionalUser", test_user_db, False)[0][0] == 1)
assert(dao.select("SELECT * FROM provisionalUser", test_user_db, False)[1][0] == 2)
assert(dao.select("SELECT * FROM provisionalUser", test_user_db, False)[0][1] == "name_test_1")
assert(dao.select("SELECT * FROM provisionalUser", test_user_db, False)[1][1] == "name_test_2")
assert(dao.deleteAll("provisionalUser", test_user_db) == True)
assert(len(dao.select("SELECT * FROM provisionalUser", test_user_db, False)) == 0)

print("Checking delete user provisionally from test user db...")
assert(dao.insertProvisionalUser2Db("delete_test_1", "delete@test.com", "123abc456def","oneTimePassforUserEmailComfirm", test_user_db) == True)
assert(len(dao.select("SELECT * FROM provisionalUser WHERE name={} AND email={}".format("'delete_test_1'", "'delete@test.com'"), test_user_db, False)) == 1)
assert(dao.deleteProvisionalUser2Db("delete_test_1", "delete@test.com", test_user_db) == True)
assert(len(dao.select("SELECT * FROM provisionalUser WHERE name={} AND email={}".format("'delete_test_1'", "'delete@test.com'"), test_user_db, False)) == 0)

print("Checking insert user into test user db...")
assert(dao.insertUser2Db("name_test_1", "email@test.com", "123abc456def", test_user_db) == True)
assert(len(dao.select("SELECT * FROM user", test_user_db, False)) == 1)
assert(dao.select("SELECT * FROM user WHERE name={} AND email={}".format("'name_test_1'","'email@test.com'"), test_user_db, False)[0][1] == "name_test_1")
assert(dao.select("SELECT * FROM user WHERE name={} AND email={}".format("'name_test_1'","'email@test.com'"), test_user_db, False)[0][2] == "email@test.com")
assert(dao.insertUser2Db("name_test_2", "email2@test.com", "789abc012def", test_user_db) == True)
assert(len(dao.select("SELECT * FROM user", test_user_db, False)) == 2)

print("Checking delete user from test user db...")
assert(dao.deleteUserFromDb("name_test_1", "email@test.com", "123abc456def", test_user_db) == True)
assert(len(dao.select("SELECT * FROM user", test_user_db, False)) == 1)
assert(dao.deleteUserFromDb("name_test_2", "email2@test.com", "789abc012def", test_user_db) == True)
assert(len(dao.select("SELECT * FROM user", test_user_db, False)) == 0)

print("Checking select and return user's info list from test user db...")
assert(dao.insertProvisionalUser2Db("sample_test_1", "sample1@test.com", "sample_auth_key1","oneTimePassforUserEmailComfirm1", test_user_db) == True)    
assert(dao.insertProvisionalUser2Db("sample_test_2", "sample2@test.com", "sample_auth_key2","oneTimePassforUserEmailComfirm2", test_user_db) == True)    
assert(dao.insertProvisionalUser2Db("sample_test_3", "sample3@test.com", "sample_auth_key3","oneTimePassforUserEmailComfirm3", test_user_db) == True)    
assert(dao.insertProvisionalUser2Db("sample_test_4", "sample4@test.com", "sample_auth_key4","oneTimePassforUserEmailComfirm4", test_user_db) == True)    
assert(dao.insertProvisionalUser2Db("sample_test_5", "sample5@test.com", "sample_auth_key5","oneTimePassforUserEmailComfirm5", test_user_db) == True)    
assert(len(dao.getProvisionalUserList()) == 5)


print("Checking isProvisionalUser...")
assert(dao.isProvisionalUser("falseconfirmpass") == False)
assert(dao.isProvisionalUser("oneTimePassforUserEmailComfirm1") == True)
assert(dao.isProvisionalUser("oneTimePassforUserEmailComfirm5") == True)

print("Cheking getUserInfoFromProvisionalUserDb...")
assert(dao.getUserInfoFromProvisionalUserDb("oneTimePassforUserEmailComfirm1")["name"] == "sample_test_1")
assert(dao.getUserInfoFromProvisionalUserDb("oneTimePassforUserEmailComfirm1")["email"] == "sample1@test.com")
assert(dao.getUserInfoFromProvisionalUserDb("oneTimePassforUserEmailComfirm1")["auth_key"] == "sample_auth_key1")

print("Checking SingUpUser...")
assert(dao.signUp("oneTimePassforUserEmailComfirm1") == True)
assert(dao.isUser("sample_auth_key1") == True)
assert(dao.signUp("oneTimePassforUserEmailComfirm5") == True)
assert(dao.isUser("sample_auth_key5") == True)

print("Finish All Test.")