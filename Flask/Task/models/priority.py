from bootstrap import db

class Priority(db.Model):
    """ Priority - Prioridades (normal,critical,warning) del
    pedido. """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    description = db.Column(db.Text)
    value = db.Column(db.Integer)
    color = db.Column(db.Unicode)

