from bootstrap import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Category(db.Model):
    """ Comments - tabla de comentarios de las tareas """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    
