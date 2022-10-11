from xml.dom import ValidationErr
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from database import my_cursor, mybd


class RegisterForm(Form):
    nombre = StringField("Nombre" ,  validators=[DataRequired()], render_kw={'placeholder':'NOMBRE DE USARIO', 'autocorrect':False})
    contrasena = PasswordField('CONTRASEÑA', validators=[DataRequired()], render_kw={'placeholder':'CONTRASEÑA', 'autocorrect':False})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder':'EMAIL', 'autocorrect':False})
    submit = SubmitField('Register')

    def validate_form(self, request):
        name = request.form.get('nombre')
        password =  request.form.get('contrasena')

        if len(name)<3:
            raise ValidationError('Name is too short')


        if not name.isalpha():
            raise ValidationError('Name error')          

        if len(password) < 8:
            raise ValidationError('Password is too short') 


        it=0;
        my_cursor.execute("select * from jugador ")
        result = my_cursor.fetchall()
        for row in result:
            print(row[1])
            if row[1] == name:
                it=it+1;
        if it != 0:
            raise ValidationError('Name already taken')   

        return True    