from flask import Flask, redirect, render_template,request, url_for
from Forms.LoginForm import LoginForm
from Forms.RegisterForm import RegisterForm


app = Flask(__name__)


@app.get('/login')
def login_template():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.post('/login')
def login():
    return render_template('inicial.html')

@app.get('/register')
def register_template():
    form = RegisterForm()
    return render_template('register.html', form=form)


@app.post('/register')
def register():
    form = RegisterForm()
    if form.validate_form(request): 
        return redirect(url_for('home')) 


@app.get('/game')
def game():
    return render_template('juego.html')

@app.get('/initial')
def home():
    return render_template('inicial.html')    

@app.get('/')
def initial():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


 