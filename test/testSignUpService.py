import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\..\\')
import signUpService as ss
import logging

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

print("Checking isSignUpUserProvisionally...")
assert(ss.isSignUpUserProvisionally("falseconfirmpass") == False)
assert(ss.isSignUpUserProvisionally(emailConfirmPass) == True)

print("Checking signUpUser...")
signup_user_name = ss.getProvisionalUserInfo(emailConfirmPass)["name"]
signup_user_email = ss.getProvisionalUserInfo(emailConfirmPass)["email"]
signup_auth_key = ss.getProvisionalUserInfo(emailConfirmPass)["auth_key"]
assert(signup_user_name == "テストユーザー")
assert(signup_user_email == "123@test.com")
assert(signup_auth_key == ss.convert2AuthKeyFromPassword("samplePassWord123"))
assert(ss.signUp(signup_user_name, signup_user_email, signup_auth_key) == True)

print("Checking isUser...")
assert(ss.isUser("123@test.com", "samplePassWord123") == True)
assert(ss.isUser("123@test.com", "samplePassWord456") == False)

print("Checking getUserInfo...")
assert(ss.getUserInfo()["name"] == "テストユーザー")
assert(ss.getUserInfo()["email"] == "123@test.com")
assert(ss.getUserInfo()["auth_key"] == ss.convert2AuthKeyFromPassword("samplePassWord123"))


print("Finish All Test.")
