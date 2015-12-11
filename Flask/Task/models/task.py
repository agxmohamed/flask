from bootstrap import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Task(db.Model):
    """ Task - Contiene la infomacion de las tareas
    a realizar """

    id = db.Column(db.Integer, primary_key=True)
    status_id = db.Column(db.Integer, ForeignKey('status.id'), default=1)
    priority_id = db.Column(db.Integer, ForeignKey('priority.id'), default=1)
    category_id = db.Column(db.Integer, ForeignKey('category.id'))
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    title = db.Column(db.Unicode)
    description = db.Column(db.Text)
    expiry_date = db.Column(db.DateTime)
    creation_date = db.Column(db.DateTime, onupdate=datetime.now)
    last_connection = db.Column(db.DateTime, default=datetime.now)

    status = db.relationship('Status')
    priority = db.relationship('Priority')
    category = db.relationship('Category')
    comment = db.relationship('Comment')
    user = db.relationship('User')