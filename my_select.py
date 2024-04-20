from sqlalchemy import func,create_engine,desc, select, and_
from main import Student, Group, Teacher, Subject, Grade
from sqlalchemy.orm import sessionmaker



engine = create_engine('postgresql://postgres:11111@localhost/postgres')
Session = sessionmaker(bind=engine)
session = Session()



def select_1():
    return session.query(Student.name, func.avg(Grade.grade).label('average_grade'))\
                  .join(Grade)\
                  .group_by(Student.name)\
                  .order_by(desc('average_grade'))\
                  .limit(5)\
                  .all()
    
    return top_students


def select_2(subject_id):
    top_student = (
        session.query(Student)
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .first()
    )
    return top_student


def select_3(subject_id):
    avg_grades_by_group = (
        session.query(Group.name, func.avg(Grade.grade).label('average_grade'))
        .select_from(Group) 
        .join(Student)
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .all()
    )
    return avg_grades_by_group


def select_4():
    avg_grade_all = (
        session.query(func.avg(Grade.grade).label('average_grade'))
        .scalar()
    )
    return avg_grade_all


def select_5(teacher_id):
    courses_taught_by_teacher = (
        session.query(Subject.name)
        .join(Teacher)
        .filter(Teacher.id == teacher_id)
        .all()
    )
    return courses_taught_by_teacher


def select_6(group_id):
    students_in_group = (
        session.query(Student)
        .filter(Student.group_id == group_id)
        .all()
    )
    return students_in_group


def select_7(group_id, subject_id):
    grades_in_group_for_subject = (
        session.query(Grade)
        .join(Student)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )
    return grades_in_group_for_subject


def select_8(teacher_id):
    avg_grade_by_teacher = (
        session.query(func.avg(Grade.grade).label('average_grade'))
        .join(Subject)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )
    return avg_grade_by_teacher


def select_9(student_id):
    courses_attended_by_student = (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .distinct()
        .all()
    )
    return courses_attended_by_student


def select_10(student_id, teacher_id):
    courses_taught_to_student_by_teacher = (
        session.query(Subject.name)
        .join(Grade)
        .join(Teacher)
        .filter(Grade.student_id == student_id, Teacher.id == teacher_id)
        .distinct()
        .all()
    )
    return courses_taught_to_student_by_teacher



if __name__=='__main__':
    #print(select_1())  # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    #print(select_2(1))   #Знайти студента із найвищим середнім балом з певного предмета
    #print(select_3(4))  #Знайти середній бал у групах з певного предмета.
    #print(select_4())   # Знайти середній бал на потоці (по всій таблиці оцінок)
    #print(select_5(4))  # Знайти які курси читає певний викладач
    #print(select_6(2))  # Знайти список студентів у певній групі
    #print(select_7(1,1))  # Знайти оцінки студентів у окремій групі з певного предмета
    #print(select_8(1))   # Знайти середній бал, який ставить певний викладач зі своїх предметів
    #print(select_9(2))  # Знайти список курсів, які відвідує певний студент
    #print(select_10(3,1))  # Список курсів, які певному студенту читає певний викладач
