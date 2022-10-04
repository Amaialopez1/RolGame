from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    nombre = StringField( validators=[DataRequired()], render_kw={'placeholder':'NOMBRE DE USARIO', 'autocorrect':False})
    contrasena = PasswordField(validators=[DataRequired()], render_kw={'placeholder':'CONTRASEÑA', 'autocorrect':False})
    submit = SubmitField('ENTRAR')

    def validate_form(self, request):
        pass