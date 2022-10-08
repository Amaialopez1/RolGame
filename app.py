from flask import Flask, redirect, render_template,request, url_for
from Forms.LoginForm import LoginForm
from Forms.RegisterForm import RegisterForm
from flask_login import login_user, LoginManager, current_user, login_required
from database import my_cursor
from user import User, users


app = Flask(__name__)
app.config['SECRET_KEY'] = 'adfadfadag';
login_manager = LoginManager(app)
login_manager.login_view= 'login_template'


@login_manager.user_loader
def load_user(id):
    for user in users:
        if user.id == id:
            return user
    return None    


@app.get('/login')
def login_template():
    form = LoginForm()
    #     print('false - login');
    return render_template('login.html', form=form)
    # if current_user.is_authenticated:
    #     print('true - login');
       # return redirect(url_for('lo'))
    # else:
    #     


@app.post('/login')
def login():
    return render_template('inicial.html')

@app.get('/register')
def register_template():
    if current_user.is_authenticated:
        print('true - register');
        return redirect(url_for('home'))
    else:
        print('false - register');
        form = RegisterForm()
        return render_template('register.html', form=form)


@app.post('/register')
def register():
    form = RegisterForm()
    if form.validate_form(request): 
        user1 = User(request.form.get('nombre'), request.form.get('contrasena'),  request.form.get('email'))
        
        sql1 = "insert into jugador(nombre_de_usario,contrasena,email) values (%s, %s, %s)";
        record1 = ( request.form.get('nombre'), request.form.get('contrasena'),  request.form.get('email'));
        my_cursor.execute(sql1,record1 );
        users.append(user1);
        
        login_user(user1, remember=True)
        if current_user.is_authenticated:
            print('true - c');
        else:
            print('false - c'); 
        # print(current_user.nombre())
        my_cursor.execute("select * from jugador")
        for jg in my_cursor:
            print(jg)
        return redirect(url_for('home')) 


@app.get('/game')
def game():
    # if current_user.is_authenticated:
    #     print('true - game');
        return render_template('juego.html')
    # else:
    #     print('false - game');    
    #     return render_template('index.html')    

    

@app.get('/initial')
def home():
    # if current_user.is_authenticated:
    #     print('true - home');
    return render_template('inicial.html') 
    # else:
    #     print('false - home');    
    #     return render_template('index.html')        

@app.get('/')
def initial():
    return render_template('index.html')

@app.get('/opciones')
def opciones():
    return render_template('opcion.html')


@app.get('/eligir')
def eligir():
    return render_template('eligir.html')


if __name__ == '__main__':

    app.run()


 