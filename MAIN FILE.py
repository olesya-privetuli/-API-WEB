from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template, Flask, request
from data import db_session, people


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
    years_of_life = StringField('Годы жизни', validators=[DataRequired()])
    grade = StringField('Звание', validators=[DataRequired()])
    place = StringField('Место смерти', validators=[DataRequired()])


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
        peop = session.query(people.People).filter(people.People.name == ''.join(request.form['name'].split()),
                                                   people.People.surname == ''.join(request.form['surname'].split()),
                                                   people.People.fathername == ''.join(
                                                       request.form['fathername'].split()))
        return render_template("people_info.html", people=peop)


@app.route('/people_info/<int:id>', methods=['GET', 'POST'])
def people_info1(id):
    if request.method == 'GET':
        session = db_session.create_session()
        peop = session.query(people.People).filter(people.People.id == id)
        return render_template("people_info.html", people=peop, title='Information')


@app.route('/all_members_adding', methods=['POST', 'GET'])
def all_members_adding():
    if request.method == 'POST':
        user = people.People()
        user.name = request.form['name']
        user.surname = request.form['surname']
        user.fathername = request.form['fathername']
        user.years_of_life = request.form['years_of_life']
        user.place_of_death = request.form['place']
        user.grade = request.form['grade']
        session = db_session.create_session()
        session.add(user)
        session.commit()
        peop = session.query(people.People).all()
        return render_template("all_members.html", people=peop, title='Полный список')


@app.route('/all_members', methods=['POST'])
def all_members():
    session = db_session.create_session()
    peop = session.query(people.People).all()
    return render_template("all_members.html", people=peop, title='Полный список')


@app.route('/admin', methods=['POST'])
def admin():
    if request.method == 'POST':
        if request.form['password'] == 'olesya' and request.form['email'] == 'olessssskayooou@mail.ru':
            form = AdminForm()
            return render_template("admin.html", form=form, title='Администрация')
        else:
            return 'incorrect email or password'


if __name__ == '__main__':
    db_session.global_init("db/people.sqlite")
    app.run(port=8080, host='127.0.0.1')
