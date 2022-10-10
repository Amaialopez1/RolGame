from flask import Flask, redirect, render_template,request, url_for, session
from itsdangerous import NoneAlgorithm
from Forms.LoginForm import LoginForm
from Forms.RegisterForm import RegisterForm
from flask_login import login_user, LoginManager, current_user, login_required
from database import my_cursor,mybd
from user import User, users
from flask_session import Session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'adfadfadag';
login_manager = LoginManager(app)
login_manager.login_view= 'login_template'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@login_manager.user_loader
def load_user(id):
    for user in users:
        if user.id == id:
            return user
    return None    


@app.get('/login')
def login_template():
    if  session.get("nombre"):
        return render_template('inicial.html')   
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

    form = LoginForm();
    it=0;
    #if form.validate_form(request):
    sql1 = "select id from jugador where nombre_de_usario = %s and contrasena = %s ";
    record1=request.form.get('nombre');
    record2=request.form.get('contrasena');
    my_cursor.execute(sql1,(record1 ,record2));
    result = my_cursor.fetchall()
    
    for row in result:
        print(row)
        it+=1;
    if it>0 :
         print('login')
         session["nombre"] = request.form.get("nombre")
         return render_template('inicial.html')     

    else:
        print('no login')     

@app.get('/register')
def register_template():
    if  session.get("nombre"):
        return render_template('inicial.html')  
    form = RegisterForm()
    return render_template('register.html', form=form)     
    # if current_user.is_authenticated:
    #     print('true - register');
    #     return redirect(url_for('home'))
    # else:
    #     print('false - register');
    #     


@app.post('/register')
def register():
    form = RegisterForm()
    if form.validate_form(request): 
        sql1 = "insert into jugador(nombre_de_usario,contrasena,email) values (%s, %s, %s)";
        record1 = ( request.form.get('nombre'), request.form.get('contrasena'),  request.form.get('email'));
        my_cursor.execute(sql1,record1 );
        mybd.commit();
        session["nombre"] = request.form.get("nombre")        
        my_cursor.execute("select * from jugador")
        for jg in my_cursor:
            print(jg)
        return redirect(url_for('home')) 


@app.get('/game')
def game():
    if not session.get("nombre"):
        print('false - game');    
        return render_template('index.html') 
    print('true - game');
    return render_template('juego.html')    
    # if current_user.is_authenticated:
    #     
    # else:
    #        

    

@app.get('/initial')
def home():
    if not session.get("nombre"):
        return render_template('index.html')   
    return render_template('inicial.html')      

@app.get('/logout')
def logout():
    session["nombre"] = None
    return render_template('index.html')


@app.get('/')
def initial():
    return render_template('index.html')

@app.get('/opciones')
def opciones():
    if not session.get("nombre"):
        return render_template('index.html')   
    return render_template('opcion.html')


@app.get('/eligir')
def eligir():
    if not session.get("nombre"):
        return render_template('index.html')   
    return render_template('eligir.html')


if __name__ == '__main__':

    app.run()


 