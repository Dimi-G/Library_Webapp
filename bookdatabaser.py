''' We create the books database using SQLalchemy, and add an initial entry. The Book class can be called in main.py for further use with Flask-Sqlalchemy'''
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import Integer, String, Float, create_engine

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__='books'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    book_title: Mapped[str]=mapped_column(String(250), nullable=False, unique=True )
    book_author: Mapped[str]=mapped_column(String(100), nullable=False)
    rating: Mapped[float]=mapped_column(Float, nullable=False)

#creates the database
engine = create_engine("sqlite:///instance/books.db")
Base.metadata.create_all(engine)  
