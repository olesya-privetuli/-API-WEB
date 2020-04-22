from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import redirect, render_template, Flask, url_for, request
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from data import db_session, users
NAMES = []


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
    if request.method == 'GET':
        return render_template('main.html', title='Поиск участников войны', form=form)


@app.route('/people_info', methods=['GET'])
def people_info():
    return 'инфа о человеке'


@app.route('/all_members', methods=['GET'])
def all_members():
    session = db_session.create_session()
    for user in session.query(users.User).all():
        NAMES.append(user.name)
    return '<br>'.join(NAMES)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = LoginForm()
    if form.password.data == 'олеся' and form.login.data == 'ol':
        return 'неверно'
    return 'верно'


if __name__ == '__main__':
    db_session.global_init("db/blogs.sqlite")
    app.run(port=8080, host='127.0.0.1')
