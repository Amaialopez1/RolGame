from wtforms import Form, RadioField
from flask import url_for

class EligirForm(Form):
   # eligir = RadioField('Eligir', choices=[('1',url_for('static', filename='img/bulbasaur_front.png')),('2',url_for('static', filename='img/charmander_front.png')), ('3',url_for('static', filename='img/squirtle_front.png'))])
    eligir = RadioField('Eligir', choices=[('1','bulbasaur'),('2','charmander'), ('3','squirtle')])