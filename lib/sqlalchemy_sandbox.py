#!/usr/bin/env python3

from sqlalchemy import (Column, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key = True)
    name= Column(String())

    def __init__ (self, name):
        self.name = name

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/db/student.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    Session = Session()
    Session.commit()