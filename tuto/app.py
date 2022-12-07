from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
import os.path
from flask_login import LoginManager




app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL']=True
app.config['SECRET_KEY'] = 'b430f4b4-0dd0-4bad-9eb5-0053680db425'
Bootstrap5(app)

def mkpath(p):
    return os.path.normpath(
        os.path.join(os.path.dirname(__file__),p))

app.config['SQLALCHEMY_DATABASE_URI']=('sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'