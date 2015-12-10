import flask
import flask.ext.sqlalchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 's4t4n-v1v3-3ntr3-n0s07r05-666-j4j4j4j4j4'
db = flask.ext.sqlalchemy.SQLAlchemy(app)