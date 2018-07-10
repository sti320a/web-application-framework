import dao
import hashlib
import uuid

def signUpUserProvisonally(username, email, password):
    
    # validation check
    if validationCheck4InsertProvisionalUser(username, email, password) == False:
        print("Validation error")
        return False
    
    # password to hash
    auth_key = covert2AuthKeyFromPassword(password)
    if auth_key == None:
        print("Auth_key is None")
        return False

    # insert user provisionally to user db
    if dao.insertProvisionalUser2Db(username, email, auth_key, email_confirm_pass) != True:
        print("InsertProvisionalUser2Db was failed")
        return False


#send email for sign up User
def sendEmail4SignUpUser(username, email, signUpUrl):
    # TODO: need to implements 
    return True


def validationCheck4InsertProvisionalUser(username, email, password):
    if (username == None) or (username == ""):
        print("Username is empty")        
        return False
    
    if (email == None) or (email == ""):
        print("Email is empty")
        return False
    
    if (password == None) or (password == ""):
        print("Password is empty")
        return False

    if len(password) <= 8:
        print("Password is too short")
        return False
    if ("@" not in email) or ("." not in email):
        print("This email is invalid")
        return False

    return True


def covert2AuthKeyFromPassword(password):
    if password == None:
        return False
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def getEmailConfirmPass():
    return str(uuid.uuid4()).replace("-","")