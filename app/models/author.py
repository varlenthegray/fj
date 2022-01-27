from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime, func, ForeignKey
from app.db.base_class import Base


class Author(Base):
    id = Column(Integer, primary_key=True, index=True)
    birthday = Column(Date, nullable=True)
    email_address = Column(String)
    experience = Column(Integer, default=0)
    hashed_password = Column(String)
    admin = Column(Boolean, default=False)
    disabled = Column(Boolean, default=False)
    moderator = Column(Boolean, default=False)
    pen_name = Column(String, nullable=True)
    username = Column(String)


class AuthorHistory(Base):
    id = Column(Integer, primary_key=True, index=True)
    action_time = Column(DateTime, default=func.now())
    action_type = Column(String)
    author_id = Column(Integer, ForeignKey("author.id"))
    ipv4 = Column(String)
    user_agent = Column(String)


class AuthorStatus(Base):
    id = Column(Integer, primary_key=True, index=True)
    automatic_books_published = Column(Integer, default=0)
    automatic_words_written = Column(Integer, default=0)
    books_read = Column(Integer, default=0)
    income = Column(Integer, default=0)
    manual_books_published = Column(Integer, default=0)
    manual_words_written = Column(Integer, default=0)
    needs_food = Column(Boolean, default=False)
    needs_hygiene = Column(Boolean, default=False)
    needs_sleep = Column(Boolean, default=False)
    needs_to_read = Column(Boolean, default=False)
    needs_to_relax = Column(Boolean, default=False)
    needs_to_research = Column(Boolean, default=False)
    time_spent_eating = Column(Integer, default=0)
    time_spent_hygiene = Column(Integer, default=0)
    time_spent_reading = Column(Integer, default=0)
    time_spent_relaxing = Column(Integer, default=0)
    time_spent_researching = Column(Integer, default=0)
    time_spent_sleeping = Column(Integer, default=0)
    author_id = Column(Integer, ForeignKey("author.id"))
    writers_block = Column(Boolean, default=False)
