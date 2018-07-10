import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\..\\')
import signUpService as ss
import logging

logging.basicConfig(filename="testSignUpServiceLog.log",level=logging.DEBUG,format='%(asctime)s %(message)s')

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

test_user_db = "testUserDb"

if os.path.exists(ROOT_DIR+'/../db/{}.db'.format(test_user_db)):
    os.remove(ROOT_DIR+'/../db/{}.db'.format(test_user_db))

assert(len(ss.getEmailConfirmPass()) == 32)
assert(ss.sendEmail4SignUpUser("testUser", "123@test.com", "1a2b3cdasdasdadewwf4d") == True)
assert(ss.signUpUserProvisionally("testUser", "123@test.com", "212131341", test_user_db) == True)


logging.info("Finish testSignUpService's All Test")