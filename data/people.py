import sqlalchemy
from .db_session import SqlAlchemyBase


class People(SqlAlchemyBase):
    __tablename__ = 'people'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    fathername = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    years_of_life = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    grade = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    place_of_death = sqlalchemy.Column(sqlalchemy.String, nullable=True)

