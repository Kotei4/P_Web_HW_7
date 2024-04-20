from faker import Faker
import random
from datetime import datetime
from main import Teacher, Subject, Student, Grade, Group
from sqlalchemy.orm import sessionmaker
from main import create_engine
from sqlalchemy.ext.declarative import declarative_base

fake = Faker()
Base = declarative_base()

def create_fake_data(session):
    groups = [Group(name=fake.word()) for _ in range(4)]
    session.add_all(groups)

    teachers = [Teacher(name=fake.name()) for _ in range(6)]
    session.add_all(teachers)

    session.commit()

    subjects = [Subject(name=fake.word(), teacher_id=random.choice(teachers).id) for _ in range(9)]
    session.add_all(subjects)

    session.commit()

    students = [Student(name=fake.name(), group_id=random.choice(groups).id) for _ in range(50)]
    session.add_all(students)

    session.commit()

    for _ in range(200):
        grade = Grade(student=random.choice(students), subject=random.choice(subjects),
                      grade=random.uniform(1, 5), date_received=datetime.now())
        session.add(grade)

    session.commit()

if __name__=='__main__':
    engine = create_engine('postgresql://postgres:11111@localhost/postgres')
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    create_fake_data(session)