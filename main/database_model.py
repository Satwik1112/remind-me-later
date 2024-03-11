"""
This will create a database and provide a interface of database to application
"""

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base


base = declarative_base()
engine = create_engine("sqlite:///db.sqlite3", echo=True)


class Remind(base):
    """creates a table for remind-me-later"""
    __tablename__ = "remind-me-later"

    rid = Column("rid", Integer, primary_key=True, autoincrement=True)
    date = Column("date", String, nullable=False)
    time = Column("time", String, nullable=False)
    message = Column("message", String, nullable=False)

    def __int__(self, **kwargs):
        self.date = kwargs.get("date")
        self.time = kwargs.get("time")
        self.message = kwargs.get("message")

    def __repr__(self):
        return f"({self.pid}. {self.date}, {self.time}, {self.message})"


base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)()
