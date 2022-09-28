from xml.dom import ValidationErr
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email, ValidationError


class RegisterForm(Form):
    nombre = StringField("Nombre" ,  validators=[DataRequired()], render_kw={'placeholder':'NOMBRE DE USARIO', 'autocorrect':False})
    contrasena = PasswordField('CONTRASEÑA', validators=[DataRequired()], render_kw={'placeholder':'CONTRASEÑA', 'autocorrect':False})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder':'EMAIL', 'autocorrect':False})
    submit = SubmitField('Register')

    def validate_form(self, request):
        name: str = request.form.get('name')
        password =  request.form.get('password')

        if len(name)<3:
            raise ValidationError('Name is too short')


        if not name.isalpha():
            raise ValidationError('Name error')          

        if len(password) < 8:
            raise ValidationError('Password is too short')    

        return True    