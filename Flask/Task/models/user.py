from bootstrap import db
from sqlalchemy import *

class User(db.Model):
    """ User - Usuarios que pueden entrar, realizar tareas
    y generar tareas """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    lastname = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    username = db.Column(db.String, unique=True, index=True)
    picture = db.Column(db.String)
