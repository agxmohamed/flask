#!/usr/bin/env python

from flask.ext import restless
from bootstrap import db, app
from models import *

# Crear tablas
db.create_all()

# Crear manager API Rest
manager = restless.APIManager(app, flask_sqlalchemy_db=db)

# Crear endpoints
manager.create_api(Task)
manager.create_api(User)
manager.create_api(Comment)

# Iniciar app
if __name__ == "__main__":
    app.run(debug=True)