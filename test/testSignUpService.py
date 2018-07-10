import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\..\\')
import signUpService as ss

assert(len(ss.getEmailConfirmPass()) == 32)
assert(ss.sendEmail4SignUpUser("testUser", "123@test.com", "http://localhost:8000/signUpFromEmail?adr=1a2b3c4d") == True)
