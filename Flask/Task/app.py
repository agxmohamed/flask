#!/usr/bin/env python

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask.ext.cors import CORS
from flask.ext import restless
from bootstrap import db, app
from models import *

# Crear tablas
db.create_all()

# Crear manager API Rest
manager = restless.APIManager(app, flask_sqlalchemy_db=db)

# Crear endpoints
manager.create_api(Task, methods=['POST', 'GET', 'DELETE', 'PUT'])
manager.create_api(User)
manager.create_api(Comment)
manager.create_api(Category)
manager.create_api(Status)
manager.create_api(Priority)

#Crear Admin
admin = Admin(app, name="Task Manager", template_mode="bootstrap3")

#Agregar Vistas del Admin
admin.add_view(ModelView(Task, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Comment, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Status, db.session))
admin.add_view(ModelView(Priority, db.session))

# Cors ->
CORS(app)


# Iniciar app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
