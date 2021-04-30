from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    #hide a warning about a feature in SQLAlchemy that we won't be using
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #set app.config['SQLALCHEMY_DATABASE_URI'] to the connection string for our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    db.init_app(app)
    migrate.init_app(app, db)

    #from app folder.models subfolder.book.py
    #import class Book
    from app.models.book import Book

    return app




