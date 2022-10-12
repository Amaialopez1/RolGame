from wtforms import Form, RadioField

class Eligi1Form(Form):
    example = RadioField('Continuar?', choices=[('Si','SI'),('No', 'No')])
