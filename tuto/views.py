from .app import app
from flask import render_template, request , redirect , url_for
from .models import get_sample , get_auteur , get_auteur2 , get_info_auteur , get_livre_auteur , get_nb_livre_auteur
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField , PasswordField
from wtforms.validators import DataRequired
from .models import *
from hashlib import sha256
from flask_login import login_user, current_user , logout_user , login_required
from .app import app,db


@app.route("/")
def home():
    return render_template(
        "home.html",
        title = "My Books",
        books = get_sample()
    )

@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = books[int(id)]
    return render_template(
        "detail.html",
        book=book)

@app.route("/auteur")
def auteur():
    return render_template(
        "auteur.html",auteurs = get_auteur()
        )

@app.route("/compte")
@login_required
def compte():
    return render_template(
        "compte.html",
        user=current_user)

class AuthorForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Name', validators=[DataRequired()])

@app.route("/edit/author/<int:id>")
@login_required
def edit_author(id):
    a = get_auteur2(id)
    f = AuthorForm(id=a.id, name=a.name)
    return render_template(
        "edit_author.html",
        author=a, form=f)

@app.route("/auteur/info/<id>")
def info_auteur(id):
    return render_template(
        "info_auteur.html",auteurs = get_info_auteur(id)
        )

@app.route("/auteur/livre/<id>")
def livre_auteur(id):
    return render_template(
        "livre_auteur.html",livres = get_livre_auteur(id),auteur = get_info_auteur(id)
        )

@app.route("/auteur/nb_livre/<id>")



    


@app.route("/save/author/", methods=['POST',])
def save_author():
    a = None
    f = AuthorForm()
    if f.validate_on_submit():
        id = int(f.id.data)
        a = get_auteur2(id)
        a.name = f.name.data
        db.session.commit()
        return redirect(url_for('afficher_author', id=a.id))
    a = get_auteur2(int[f.id.data])
    return render_template(
        "edit_author.html",
        author=a, form=f)

@app.route("/author/<int:id>")
def afficher_author(id):
    a = get_auteur2(id)
    return render_template(
        "info_auteur.html",
        author=a)

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    next = HiddenField()

    def get_authenticated_user(self):
        user = User.query.get(self.username.data)
        if user is None:
            return None
        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest()
        if user.password == passwd:
            return user
        return None

@app.route("/login/", methods=['GET', 'POST'])
def login():
    f = LoginForm()
    if not f.is_submitted():
        f.next.data = request.args.get('next')
    elif f.validate_on_submit():
        user = f.get_authenticated_user()
        if user: 
            login_user(user)
            next = f.next.data or url_for('home') 
            return redirect(next)
    return render_template(
        "login.html",
        form=f)

    

@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for('home'))

class BookForm(FlaskForm):
    id = HiddenField('id')
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])

# @app.route("add/favorite/", methods=['POST',])
# @login_required
# def add_favorite():
#     f = BookForm()
#     if f.validate_on_submit():
#         id = int(f.id.data)
#         title = f.title.data
#         author = f.author.data
#         b = Favorite(id=id, title=title, author=author)
#         db.session.add(b)
#         db.session.commit()
#         return redirect(url_for('home'))

# recupeer les données de la barre de recherche et les afficher dans la page resultat.html

class SearchForm(FlaskForm):
    search = StringField('search', validators=[DataRequired()])

@app.route("/search/", methods=['POST'])
def search():
    f = SearchForm()
    mot = f.search.data
    print(mot)
    print(type(mot))
    books= Book.query.filter(Book.title.like('%'+mot+'%')).all()
    print(books)
    return render_template(
        "resultat.html",
        form=f, result=books)
        
    
        
        


        


