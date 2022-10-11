from re import L
from flask import Flask, redirect, render_template,request, url_for, session
from itsdangerous import NoneAlgorithm
from numpy import void
from Forms.LoginForm import LoginForm
from Forms.RegisterForm import RegisterForm
from database import my_cursor, mybd
from flask_session import Session
from Forms.Cambiar_nombre import camb
import sys

if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    import collections
    setattr(collections, "MutableMapping", collections.abc.MutableMapping)
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adfadfadag';
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

socketio = SocketIO(app)

@socketio.on('enemigo')
def enemigo():
    print("aperece enemigo")

@app.get('/login')
def login_template():
    if  session.get("nombre"):
        return render_template('inicial.html')   
    form = LoginForm()
    return render_template('login.html', form=form)

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

    form = camb();     
    return render_template('opcion.html', form=form)

@app.post('/opciones')
def opc():
    if request.form.get('nombre').isalpha():
        form = camb();
        if  form.validate_form(request):
            my_cursor.execute("update jugador set nombre_de_usario = %s where nombre_de_usario = %s ", (request.form.get('nombre'),session.get("nombre")));
            mybd.commit();
            session["nombre"] = request.form.get('nombre');
            my_cursor.execute("select * from jugador")
            for jg in my_cursor:
               print(jg)
    return render_template('inicial.html')         

@app.get('/eligir')
def eligir():
    if not session.get("nombre"):
        return render_template('index.html')   
    return render_template('eligir.html')

@socketio.on('enemigo')
def enemigo():
    print('enemigo')

@socketio.on('connect')
def connect():
    session['sid'] = request.sid

if __name__ == '__main__':

    socketio.run(app, allow_unsafe_werkzeug=True)

