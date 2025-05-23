#!/usr/bin/env python3

from sqlalchemy import (Column, Integer, String, create_engine, desc, func)
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
    session = Session()

#Creating Record

    # student1 = Student("Belinder") #Instance
    # student2 = Student("Kylian")
    # student3 = Student("Mellon")  
    # # session.add(student1) # add single

    # session.bulk_save_objects([student1, student2, student3]) 
    # # using to add many intance but the downside is that you can't access the ID

    # session.commit()
# -----------------------------------------------------------------------

# Read Records
    # students = session.query(Student).all()
    # print([student.name for student in students])
    
    # filters

    # student = session.query(Student).filter(Student.id == 2).first()
    # print(student.name)

    #update
    
    # session.query(Student).filter(Student.id == 2).update(
    #     {Student.name: "Julianna"}
    # )
    # session.commit()
    # student = session.query(Student).filter_by(id=2).first()
    # print(student.name)

    # ordering and limiting
    student_by_name = [student for student in session.query(
        Student.name).order_by(desc(Student.name)).limit(1)]
    
    print(student_by_name)

    