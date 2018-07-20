import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\..\\')
import loginService as ls
import signUpService as ss
import dao
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

test_user_db = "testUserDb"

if os.path.exists(ROOT_DIR+'/../db/{}.db'.format(test_user_db)):
    os.remove(ROOT_DIR+'/../db/{}.db'.format(test_user_db))

print("Preparing user login...")
sample_auth_key = ss.covert2AuthKeyFromPassword("sample_password")
print("auth_key:"+sample_auth_key)
assert(dao.insertProvisionalUser2Db("login_test_user", "login@test.com", sample_auth_key, "oneTimePassforUserEmailComfirm", test_user_db) == True)    
assert(dao.isProvisionalUser("oneTimePassforUserEmailComfirm") == True)
assert(dao.signUp("oneTimePassforUserEmailComfirm") == True)
print("Complete preparing.")

print("Checking login...")
assert(ls.login("login@test.com", "sample_password") == True)



print("Finish all test.")

if os.path.exists(ROOT_DIR+'/../db/{}.db'.format(test_user_db)):
    os.remove(ROOT_DIR+'/../db/{}.db'.format(test_user_db))