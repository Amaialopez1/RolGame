from flask import Flask, redirect, render_template
from Forms.LoginForm import LoginForm
from Forms.RegisterForm import RegisterForm


app = Flask(__name__)


@app.get('/login')
def login_template():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.post('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.get('/register')
def register_template():
    form = RegisterForm()
    return render_template('register.html', form=form)


@app.post('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run()

 