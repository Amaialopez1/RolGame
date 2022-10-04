from flask import Flask, redirect, render_template
from Forms.LoginForm import LoginForm
from Forms.RegisterForm import RegisterForm

app = Flask(__name__, template_folder='templates')


@app.get('/')
def main_template():
    return render_template('auth/gamePage.html')


@app.get('/home')
def home_template():
    return render_template('home/initial.html')


@app.get('/login')
def login_template():
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@app.post('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@app.get('/registro')
def register_template():
    form = RegisterForm()
    return render_template('auth/register.html', form=form)


@app.post('/registro')
def register():
    form = RegisterForm()
    return render_template('auth/register.html', form=form)


if __name__ == '__main__':
    app.run()
