from .app import db
from flask_login import UserMixin
from .app import login_manager
# import yaml , os.path

# Books = yaml.safe_load(open(os.path.join(os.path.dirname(__file__),"data.yml")))

# i=0
# for book in Books:
#     book['id'] = i
#     i+=1

# def get_sample():
#     return Books[0:10]

class User(db.Model,UserMixin):
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))

    def get_id(self):
        return self.username

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __repr__(self) -> str:
        return "<Author: %d %s>" % (self.id , self.name)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    title = db.Column(db.String(100))
    img = db.Column(db.String(200))
    url = db.Column(db.String(200))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", backref=db.backref("books", lazy="dynamic"))

def __repr__ (self ):
    return "<Book (%d) %s>" % (self.id , self.title)

def get_sample():
    return Book.query.limit(10).all()

def get_auteur():
    return Author.query.all()

def get_auteur2(id):
    return Author.query.get(id)

def get_info_auteur(id):
    return Author.query.filter(Author.id == id).all()

def get_livre_auteur(id):
    return Book.query.filter(Book.author_id == id).all()

def get_nb_livre_auteur(id):
    id_a = int(id) + 1
    return Book.query.filter_by(Book.author_id == id_a).all()

@login_manager.user_loader
def load_user(username):
    return User.query.get(username) 