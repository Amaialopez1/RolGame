from re import L
from xml.dom import ValidationErr
from flask import Flask, redirect, render_template,request, url_for, session
from itsdangerous import NoneAlgorithm
from numpy import void
from Forms.LoginForm import LoginForm
from Forms.RegisterForm import RegisterForm
from database import my_cursor,mybd
from flask_session import Session
from Forms.Cambiar_nombre import  camb
from Forms.Eligir1Form import Eligi1Form
from Forms.EligirForm import EligirForm
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

@app.route('/eligir1',methods=['POST','GET'])
def hello_world():
    form = Eligi1Form()
    if request.method == 'POST':
        SelectedValue = request.form
        print("================================")
        print(SelectedValue)
        data = request.form.to_dict();
        print(request.form.to_dict())
        print(data['example'])
        
        print('=======')
        if data['example'] ==  'No':
            print("no");
        else:
            print("FUCK")

    return render_template('eligir1.html', form=form)
    

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
         sql2="select id from jugador where nombre_de_usario = %s; ";
         record2 = (request.form.get('nombre'),)
         my_cursor.execute(sql2,record2 )  
         result = my_cursor.fetchone();
        

         session["id"]=result[0];
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
        # my_cursor.execute("select * from jugador")
        # for jg in my_cursor:
        #     print(jg)
        sql2="select id from jugador where nombre_de_usario = %s; ";
        record2 = (request.form.get('nombre'),)
        my_cursor.execute(sql2,record2 )  
        result = my_cursor.fetchone();
        

        session["id"]=result[0];
        
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
    form = EligirForm();     
    return render_template('eligir.html')

@app.post('/eligir')
def eligir_post():
    form = EligirForm();   
   
    sql1 =" insert into pokemon(tipo_de_pokemon)  values (%s)";
    record1 = (request.form['eligir'],)
    print(request.form['eligir']);
    my_cursor.execute(sql1,record1)
    mybd.commit();
    my_cursor.execute("select * from pokemon")
    for jg in my_cursor:
         print(jg)

    print(session.get("id"));
    sql2="select id_coach from coach where id_jugador = %s; ";
    record2 = (session.get("id"),)
    my_cursor.execute(sql2,record2 )  
    result = my_cursor.fetchone();

    my_cursor.execute("SET GLOBAL FOREIGN_KEY_CHECKS=0;")

    sql3="select id_pokemon from pokemon order by id_pokemon desc ";
    my_cursor.execute(sql3)  
    result3 = my_cursor.fetchone();
    if result3 != None:
        id_pokemon= result3[0]
    print(result3[0]);
    my_cursor.reset();



    if result== None:  
        sql4 = "insert coach(id_jugador, id_pokemon ) values(%s,%s); ";
        record4 = (session.get("id"), id_pokemon, )
        print(record4)
        my_cursor.execute(sql4,record4)
        mybd.commit();
        my_cursor.execute("select * from coach")
        for jg in my_cursor:
             print(jg)
        mybd.commit();     
    else:
        sql5 = "select id_pokemon from coach where id_jugador = %s";
        record5 = (session.get("id"),)
        my_cursor.execute(sql5, record5)  
        result5 = my_cursor.fetchone();
        id_pokemon_for_delete= result5[0]
        print(result5[0]);
        my_cursor.reset();
        print("tut")

        sql6 = "update coach set id_pokemon = %s where id_jugador = %s";
        record6 = ( id_pokemon,session.get("id"),  )
        my_cursor.execute(sql6,record6)
        mybd.commit()
        print("tut1")

        sql7 = "delete from pokemon where id_pokemon = %s";
        record7 = (id_pokemon_for_delete, )
        my_cursor.execute(sql7,record7)
        mybd.commit()

        my_cursor.execute("select * from coach")
        for jg in my_cursor:
             print(jg)

        print("si")    
    

    

#   my_cursor.execute("select ")
    return render_template('eligir.html', form = form)

@socketio.on('connect')
def connect():
    session['sid'] = request.sid 

    
if __name__ == '__main__':
    # socketio.run(app)
    app.run()
