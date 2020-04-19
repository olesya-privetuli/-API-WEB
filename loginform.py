from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import redirect, render_template, Flask, url_for
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session


class LoginForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    fathername = StringField('Отчество', validators=[DataRequired()])
    to_find = SubmitField('Поиск')
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('main.html', title='Поиск участников войны', form=form)


@app.route('/people_info', methods=['GET'])
def people_info():
    return 'инфа о челике'


@app.route('/all_members', methods=['GET'])
def all_members():
    return 'список'


@app.route('/admin', methods=['GET'])
def admin():
    return 'я зеся главный'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
