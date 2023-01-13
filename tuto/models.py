from .app import db
from flask_login import UserMixin
from .app import login_manager

class User(db.Model,UserMixin):
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))

    def get_id(self):
        return self.username

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __repr__(self) -> str:
        return "%s" % (self.name)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    title = db.Column(db.String(100))
    img = db.Column(db.String(200))
    url = db.Column(db.String(200))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", backref=db.backref("books", lazy="dynamic"))

class Favorite(db.Model):
    user_id = db.Column(db.String(80), db.ForeignKey("user.username") , primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), primary_key=True)
    user = db.relationship("User", backref=db.backref("favorites", lazy="dynamic"))
    book = db.relationship("Book", backref=db.backref("favorites", lazy="dynamic"))

def __repr__ (self ):
    return "<Book (%d) %s>" % (self.id , self.title)

def get_sample():
    return Book.query.all()

def get_auteur():
    return Author.query.all()

def get_livre(id):
    return Book.query.get(id)

def get_auteur2(id):
    return Author.query.get(id)

def get_info_auteur(id):
    return Author.query.filter(Author.id == id).all()

def get_livre_auteur(id):
    return Book.query.filter(Book.author_id == id).all()

def get_nb_livre_auteur(id):
    id_a = int(id) + 1
    return Book.query.filter_by(Book.author_id == id_a).all()

def ajouter_favoris(idUser,idLivre):
    fav = Favorite(user_id=idUser,book_id=idLivre)
    db.session.add(fav)
    db.session.commit()

def supprimer_favoris(idUser,idLivre):
    fav = Favorite.query.filter_by(user_id=idUser,book_id=idLivre).first()
    db.session.delete(fav)
    db.session.commit()

def get_favoris(idUser):
    return Favorite.query.filter_by(user_id=idUser).all()

@login_manager.user_loader
def load_user(username):
    return User.query.get(username) 

def get_favorites_books(user_id):
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    books = []
    for favoris in favorites:
        books.append(get_livre(favoris.book_id))
    return books


