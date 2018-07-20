#! python3
# loginService.py
import signUpService as ss
import dao

def login(email, password):
    auth_key = ss.covert2AuthKeyFromPassword(password)
    print("auth_key:"+auth_key)
    if dao.isUser(email, auth_key):
        return dao.getUserInfo(email, auth_key) 
    return False