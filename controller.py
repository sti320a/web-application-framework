#! python3
# controller.py

from flask import Flask, session, redirect, render_template, request
import signUpService
import const

app = Flask(__name__)

@app.route('/')
def showIndexView():
    return render_template("index.html")

@app.route('/login')
def showLoginView():
    return render_template('login.html')

@app.route('/signup')
def showSignUpView():
    return render_template('signup.html')

@app.route('/provisional_signup', methods=['POST'])
def signupUserProvisionally():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        signUpService.signUpUserProvisionally(username, email, password, const.DB_FILE_NAME)
        return render_template('provisional_signup_completed.html', email=email)
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


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
