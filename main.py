from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from bookdatabaser import Book
from bookforms import AddForm, EditForm, SearchForm
from datetime import datetime
from googlebooks_api import BookApi
import os

app = Flask(__name__)
bootstrap=Bootstrap5(app)

#connecting Flask_sqlalchemy with the database and sqlalchemy class created in bookdatabaser
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", "sqlite:///books.db")
db = SQLAlchemy(app)
db.Model = Book

year=datetime.now().year #get's passed to the template, for the html footer to be up-to-date

#Routing the app, assigning methods to display entries, add, edit and delete them
@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.book_author)).scalars()
    return render_template("index.html", all_books=all_books, year=year)

@app.route("/add", methods = ["GET", "POST"])
def add():
    form=AddForm(meta={'csrf': False}) #disabling the csrf check, since we are not interested in such protection for this app. If needed,delete boolean (the csrf check is default) and assign an app.config['SECRET_KEY']
    if form.validate_on_submit(): # meaning it is a POST request and without errors: we add the completed form fields to the database
        new_book=Book(
            book_title = form.book_title.data,
            book_author = form.book_author.data,
            rating=form.rating.data
            )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))            
    return render_template("add.html", form=form, year=year)

@app.route('/edit/<int:id>', methods = ["GET", "POST"])
def edit(id):
    book = db.session.query(Book).get(id)
    edit_form=EditForm(meta={'csrf': False})
    if edit_form.validate_on_submit():
        new_rating=edit_form.new_rating.data
        book.rating = new_rating   
        db.session.commit()  
        return redirect(url_for('home'))      
    return render_template("edit.html", edit_form=edit_form, book=book, year=year)

@app.route('/delete/<int:id>')
def delete(id):
    book = db.session.query(Book).get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/search/', methods=["GET", "POST"])
def search():
    search_form = SearchForm(meta={'csrf': False})
    book_api = BookApi()
    if search_form.validate_on_submit():
        title=search_form.search_title.data
        volumes, ids = book_api.find_books(title)
        image_links = [book_api.find_by_id(id) for id in ids]
        zipped_list= zip(volumes, image_links)
        
        return render_template("googlebooks.html",zipped_list=zipped_list, year=year)
    return render_template("search.html", form=search_form, year=year)

if __name__ == "__main__":
    app.run(debug=True) #set False for deploy

    