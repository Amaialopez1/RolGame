from xml.dom import ValidationErr
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email, ValidationError, Length
from database import my_cursor,mybd


class RegisterForm(Form):
    nombre = StringField("Nombre" ,  validators=[DataRequired(),Length(min=3)], render_kw={'placeholder':'NOMBRE DE USARIO', 'autocorrect':False})
    contrasena = PasswordField('CONTRASEÑA', validators=[DataRequired(), Length(min=8)], render_kw={'placeholder':'CONTRASEÑA', 'autocorrect':False})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder':'EMAIL', 'autocorrect':False})
    submit = SubmitField('Register')

    def validate_form(self, request):
        name = request.form.get('nombre')

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