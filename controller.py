#! python3
# controller.py

from flask import Flask, session, redirect, render_template, request, make_response
import signUpService
import loginService
import dao
import const

db_file_name = const.DB_FILE_NAME

app = Flask(__name__)
app.secret_key = "vjabpivp3rubvpiebvASDwibp"


@app.route('/')
def showIndexView():
    return render_template("index.html", username=getLoginStatus())

@app.route('/login')
def showLoginView():
    return render_template('login.html', username=getLoginStatus())

@app.route('/logout')
def logout():
    return render_template("index.html", username=getLoginStatus())

@app.route('/login_check', methods=['POST'])
def loginCheck():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        login_info = loginService.login(email, password)

        if login_info != False:
            session["username"] = login_info["name"]
            return redirect("/?logined")
        else:
            return redirect("/login")
    else:
        return redirect("/login")

@app.route('/signup', methods=['GET'])
def showSignUpView():
    return render_template('signup.html', username=getLoginStatus())


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
            return render_template("signup_fail.html",username=getLoginStatus())
    else:
        print("method is invalid")
    return render_template('signup_complete.html', username=getLoginStatus())


@app.route('/provisional_signup', methods=['POST'])
def signupUserProvisionally():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # validation check
        validation_results = signUpService.validationCheck4InsertProvisionalUser(username, email, password);
        if len(validation_results) >= 1:
            return render_template('signup.html', validation_results=validation_results, username=getLoginStatus(), email=email)    

        signUpService.signUpUserProvisionally(username, email, password, db_file_name)
        return render_template('provisionalSignupCompleted.html', username=getLoginStatus(), email=email)
    else:
        return redirect('/signup')


@app.route('/contents')
def showContentsUpView():
    return render_template('contents.html', username=getLoginStatus())

@app.route('/account')
def showAccountView():
    return render_template('account.html', username=getLoginStatus())

@app.route('/user')
def showUserView():
    return render_template('user.html', username=getLoginStatus())

@app.route('/edit_profile')
def showEditProfileView():
    return render_template('editProfile.html', username=getLoginStatus())

@app.route('/AFewbeon32GhOi90ZXAccountAdmin')
def showAccountAdminView():
    user_list = dao.getUserList()
    return render_template('accountAdmin.html', username=getLoginStatus(), user_list=user_list)


def getLoginStatus():
    if session.get("username") != None and session.get("username") != "":
        username = session["username"]
        return username
    else:
        return False



if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
