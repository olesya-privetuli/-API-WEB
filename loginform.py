from flask_wtf import FlaskForm
from wtforms import TextField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import redirect, render_template, Flask, url_for, request
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import requests
from data import db_session, users
NAMES = []


class LoginForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    fathername = StringField('Отчество', validators=[DataRequired()])
    to_find = SubmitField('Поиск')
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])


class AdminForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    fathername = StringField('Отчество', validators=[DataRequired()])
    add = SubmitField('Добавить')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('main.html', title='Поиск участников войны', form=form)


@app.route('/people_info', methods=['POST'])
def people_info():
    session = db_session.create_session()
    if request.method == 'POST':
        peop = session.query(users.User).filter(users.User.name == ''.join(request.form['name'].split()),
                                                users.User.surname == ''.join(request.form['surname'].split()),
                                                users.User.fathername == ''.join(request.form['fathername'].split()))
        return render_template("people_info.html", people=peop)


@app.route('/people_info/<int:id>', methods=['GET', 'POST'])
def people_info1(id):
    if request.method == 'GET':
        session = db_session.create_session()
        peop = session.query(users.User).filter(users.User.id == id)
        return render_template("people_info.html", people=peop, title='Information')


@app.route('/all_members', methods=['POST', 'GET'])
def all_members():
    if request.method == 'POST':
        print(request.form.get('name'))
        session = db_session.create_session()
        peop = session.query(users.User).all()
        return render_template("all_members.html", people=peop, title='Полный список')
    elif request.method == 'GET':
        session = db_session.create_session()
        peop = session.query(users.User).all()
        return render_template("all_members.html", people=peop, title='Полный список')


@app.route('/admin', methods=['POST'])
def admin():
    if request.method == 'POST':
        if request.form['password'] == 'olesya' and request.form['email'] == 'olessssskayooou@mail.ru':
            form = AdminForm()
            return render_template("admin.html", form=form)
        else:
            return 'incorrect email or password'


if __name__ == '__main__':
    db_session.global_init("db/people.sqlite")
    app.run(port=8080, host='127.0.0.1')
