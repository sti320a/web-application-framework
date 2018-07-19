import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\..\\')
import signUpService as ss
import logging
import dao

#logging.basicConfig(filename="testSignUpServiceLog.log",level=logging.DEBUG,format='%(asctime)s %(message)s')

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

test_user_db = "testUserDb"

if os.path.exists(ROOT_DIR+'/../db/{}.db'.format(test_user_db)):
    os.remove(ROOT_DIR+'/../db/{}.db'.format(test_user_db))

print("Checking getEamilConfirmPass...")
emailConfirmPass = ss.getEmailConfirmPass()
assert(len(emailConfirmPass) == 32)

print("Checking sendEmail4SignUpUser...")
assert(ss.sendEmail4SignUpUser("testUser", "123@test.com", "1a2b3cdasdasdadewwf4d") == True)

print("Checking signUpUserProvisionally...")
assert(ss.signUpUserProvisionally("testUser", "123@test.com", "samplePassWord123", test_user_db) == True)

print("Checking sendEmail4SignUpUser...")
assert(ss.sendEmail4SignUpUser("テストユーザー", "123@test.com", "http://12345/signUpConfimr?p={}".format(emailConfirmPass)))




print("Finish All Test.")
