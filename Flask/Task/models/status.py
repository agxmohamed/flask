from bootstrap import db

class Status(db.Model):
    """ Status - Contiene el estado de una tarea """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    description = db.Column(db.Text)
