from bootstrap import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Task(db.Model):
    """ Task - Contiene la infomacion de las tareas
    a realizar """

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, ForeignKey('status.id'), default=1)
    priority = db.Column(db.Integer, ForeignKey('priority.id'), default=1)
    category = db.Column(db.Integer, ForeignKey('category.id'))
    comment = db.Column(db.Integer, ForeignKey('comment.id'))
    user = db.Column(db.Integer, ForeignKey('user.id'))
    title = db.Column(db.Unicode)
    description = db.Column(db.Text)
    expiry_date = db.Column(db.DateTime)
    creation_date = db.Column(db.DateTime, onupdate=datetime.now)
    last_connection = db.Column(db.DateTime, default=datetime.now)
