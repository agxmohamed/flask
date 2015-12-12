from bootstrap import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Comment(db.Model):
    """ Comment - tabla de comentarios de las tareas """

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, ForeignKey('task.id'))
    content = db.Column(db.Unicode)
    date = db.Column(db.DateTime, default=datetime.now)

    task = db.relationship('Task')