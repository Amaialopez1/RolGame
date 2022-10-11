from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from database import my_cursor, mybd


class camb(Form):
    nombre = StringField("Nombre", validators=[DataRequired()],
                         render_kw={'placeholder': 'NOMBRE DE USARIO', 'autocorrect': False})
    submit = SubmitField('Cambiar nombre')

    def validate_form(self, request):
        name: str = request.form.get('nombre')

        if len(name) < 3:
            raise ValidationError('Name is too short')

        if not name.isalpha():
            raise ValidationError('Name error')

        it = 0;
        my_cursor.execute("select * from jugador ")
        result = my_cursor.fetchall()
        for row in result:
            print(row[1])
            if row[1] == name:
                it = it + 1;
        if it != 0:
            raise ValidationError('Name already taken')

        return True
