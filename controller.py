#! python3
# controller.py

from flask import Flask, session, redirect, render_template, request, make_response
import signUpService
import loginService
import dao
import const
import werkzeug
import sys, os
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

db_file_name = const.DB_FILE_NAME
db_of_moives = "movie"
MOVIE_UPLOAD_PATH = "./static/movie/"

app = Flask(__name__)
app.secret_key = "vjabpivp3rubvpiebvASDwibp"


@app.route('/')
def showIndexView():
    postList = dao.getAllMovies(db_of_moives)
    return render_template("index.html", username=getLoginUser(), postList=postList)

@app.route('/login')
def showLoginView():
    return render_template('login.html', username=getLoginUser())

@app.route('/logout')
def logout():
    session.pop("username", None)
    return render_template("index.html", username=getLoginUser())

@app.route('/login_check', methods=['POST'])
def loginCheck():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        login_info = loginService.login(email, password)

        if login_info != False:
            session["username"] = login_info["name"]
            session["userid"] = login_info["id"]
            return redirect("/?logined")
        else:
            return redirect("/login")
    else:
        return redirect("/login")

@app.route('/signup', methods=['GET'])
def showSignUpView():
    return render_template('signup.html', username=getLoginUser())


@app.route('/signup_complete')
def signUpConfirm():
    if request.method == "GET":
        confirm_pass = request.args.get("p")
        if dao.isProvisionalUser(confirm_pass):
            user_info = dao.getUserInfoFromProvisionalUserDb(confirm_pass)
            name = user_info['name']
            email = user_info['email']
            auth_key = user_info['auth_key']
            dao.insertUser2Db(name, email, auth_key, db_file_name)
        else:
            return render_template("signup_fail.html",username=getLoginUser())
    else:
        print("method is invalid")
    return render_template('signup_complete.html', username=getLoginUser())


@app.route('/provisional_signup', methods=['POST'])
def signupUserProvisionally():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # validation check
        validation_results = signUpService.validationCheck4InsertProvisionalUser(username, email, password);
        if len(validation_results) >= 1:
            return render_template('signup.html', validation_results=validation_results, username=getLoginUser(), email=email)    

        signUpService.signUpUserProvisionally(username, email, password, db_file_name)
        return render_template('provisionalSignupCompleted.html', username=getLoginUser(), email=email)
    else:
        return redirect('/signup')

@app.route('/post')
def showPostView():
    if request.method == "GET":
        return render_template('post.html', username=getLoginUser())
    
@app.route('/post', methods=['POST'])
def runPost():    
    if request.method == "POST":
        
        if 'upload_file' not in request.files:
            print("uploadfile is None")
            return redirect('/')

        file = request.files['upload_file']
        fileName = file.filename

        if '' == fileName:
            print("filename is empty")
            return redirect('/')

        userid = getLoginUserid()
        title = request.form['title']
        comment = request.form['comment']
        saveFileName = datetime.now().strftime("%Y%m%d_%H%M%S_") + werkzeug.utils.secure_filename(fileName)
        file.save(os.path.join(MOVIE_UPLOAD_PATH, saveFileName))

        dao.insertMovie(db_of_moives, userid, title, comment,os.path.join(MOVIE_UPLOAD_PATH, saveFileName))

        print("success upload")

        return redirect('/')


@app.route('/contents')
def showContentsUpView():
    
    if request.method == "GET":
        contents_id = request.args.get("id")
        contents_info = dao.getContentsFromId(db_of_moives,int(contents_id))

    return render_template('contents.html', username=getLoginUser(), contents_info=contents_info)

@app.route('/account')
def showAccountView():
    return render_template('account.html', username=getLoginUser())

@app.route('/user')
def showUserView():
    return render_template('user.html', username=getLoginUser())

@app.route('/edit_profile')
def showEditProfileView():
    return render_template('editProfile.html', username=getLoginUser())

@app.route('/AFewbeon32GhOi90ZXAccountAdmin')
def showAccountAdminView():
    user_list = dao.getUserList()
    return render_template('accountAdmin.html', username=getLoginUser(), user_list=user_list)


def getLoginUser():
    if session.get("username") != None and session.get("username") != "":
        username = session["username"]
        return username
    else:
        return False

def getLoginUserid():
    if session.get("userid") != None and session.get("userid") != "":
        userid = session["userid"]
        return userid
    else:
        return False


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
