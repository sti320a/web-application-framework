#! python3
# controller.py

from flask import Flask, session, redirect, render_template, request

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



if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
