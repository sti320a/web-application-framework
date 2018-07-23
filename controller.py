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
    if session.get("username") != None and session.get("username") != "":
        username = session["username"]
        print("username:"+username)
        return render_template("index.html", username=username)
    return render_template("index.html")

@app.route('/login')
def showLoginView():
    return render_template('login.html')

@app.route('/logout')
def logout():
    if session.get("username") != None and session.get("username") != "":
        session.pop("username", None)
    return render_template("index.html", username=None)

@app.route('/login_check', methods=['POST'])
def loginCheck():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        login_info = loginService.login(email, password)

        if login_info != False:
            print("login seccess")
            session["username"] = login_info["name"]
            print(login_info["name"])
            return redirect("/?logined")
        else:
            print("Cannot get login_info")
            return redirect("/login")
    else:
        print("method is invalid")
        return redirect("/login")

@app.route('/signup', methods=['GET'])
def showSignUpView():
    return render_template('signup.html')

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
            print("sigunp_completed")
        else:
            print("signup_failed")
            return render_template("signup_fail.html")
    else:
        print("method is invalid")
    return render_template('signup_complete.html')

@app.route('/provisional_signup', methods=['POST'])
def signupUserProvisionally():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # validation check
        validation_results = signUpService.validationCheck4InsertProvisionalUser(username, email, password);
        if len(validation_results) >= 1:
            return render_template('signup.html', validation_results=validation_results, username=username, email=email)    

        signUpService.signUpUserProvisionally(username, email, password, db_file_name)
        return render_template('provisionalSignupCompleted.html', email=email)
    else:
        return redirect('/signup')


@app.route('/contents')
def showContentsUpView():
    return render_template('contents.html')

@app.route('/account')
def showAccountView():
    return render_template('account.html')

@app.route('/user')
def showUserView():
    return render_template('user.html')

@app.route('/edit_profile')
def showEditProfileView():
    return render_template('editProfile.html')

@app.route('/AFewbeon32GhOi90ZXAccountAdmin')
def showAccountAdminView():
    user_list = dao.getUserList()
    print("controller.showAccountAdminView:"+str(user_list))
    return render_template('accountAdmin.html', user_list=user_list)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
