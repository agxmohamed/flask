from bootstrap import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Category(db.Model):
    """ Comments - tabla de comentarios de las tareas """

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.now, index=True)
    task = db.Column(db.Integer, ForeignKey('task.id'))
