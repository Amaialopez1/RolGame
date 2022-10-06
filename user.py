from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import uuid



users=[];





def get_user(nombre):
    for user in users:
        if user.nombre == nombre:
            return user
    return None        



class User(UserMixin):
    def __init__(self, nombre, contrasena, email):
        self.id= uuid.uuid4();
        self.nombre=nombre;
        self.contrasena=generate_password_hash(contrasena);
        self.email=email;

    def check_password(self, password):
        return check_password_hash(self.password. password)

    def is_authenticated(self):
        return True
    

    # def __repr__(self):
    #     return "User:{}".format(self.name)

    # def to_json(self):
    #     return{
    #         'id':self.id,
    #         'name':self.name,
    #         'password':self.password,
    #         'admin':self.is_admin
    #     }    
