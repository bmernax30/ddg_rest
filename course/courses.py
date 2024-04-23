# users.py
from flask import abort, make_response
from config import db_course
from models import Course, courses_schema, course_schema

def read_all():
    courses = Course.query.all()
    return courses_schema.dump(courses)

def create(course):
    #This needs to be changed for course create
    course_id = course.get("id")
    existing_course = Course.query.filter(Course.id == course_id).one_or_none()

    if existing_course is None:
        new_course = course_schema.load(course, session=db_course.session)
        db_course.session.add(new_course)
        db_course.session.commit()
        return course_schema.dump(new_course), 201
    else:
        abort(404 ,f"Course with id {course} already exists")

def read_one(course_id):
    #This needs to be changed to include a search for the layout name
    course = Course.query.filter(Course.id == course_id).one_or_none()
    if course is not None:
        return course_schema.dump(course)
    else:
        abort(404, f"Course with course id {course_id} not found")

def update_one_value(course_id,course,value):
    existing_course = Course.query.filter(Course.id == course_id).one_or_none()
    if existing_course:
        update_course = course_schema.load(course, session=db_course.session)
        print("WE made it!")
        print(value)
        if value == 1:
            existing_course.course_name = update_course.course_name
        elif value == 2:
            existing_course.layout_name = update_course.layout_name
        elif value == 3:
            existing_course.par = update_course.par
        elif value == 4:
            existing_course.length = update_course.length
        elif value == 5:
            existing_course.num_holes = update_course.num_holes
        elif value == 6:
            existing_course.hole1_id = update_course.hole1_id
        elif value == 7:
            existing_course.hole2_id = update_course.hole2_id
        elif value == 8:
            existing_course.hole3_id = update_course.hole3_id
        elif value == 9:
            existing_course.hole4_id = update_course.hole4_id
        elif value == 10:
            existing_course.hole5_id = update_course.hole5_id
        elif value == 11:
            existing_course.hole6_id = update_course.hole6_id
        elif value == 12:
            existing_course.hole7_id = update_course.hole7_id
        elif value == 13:
            existing_course.hole8_id = update_course.hole8_id
        elif value == 14:
            existing_course.hole9_id = update_course.hole9_id
        elif value == 15:
            existing_course.hole10_id = update_course.hole10_id
        elif value == 16:
            existing_course.hole11_id = update_course.hole11_id
        elif value == 17:
            existing_course.hole12_id = update_course.hole12_id
        elif value == 18:
            existing_course.hole13_id = update_course.hole13_id
        elif value == 19:
            existing_course.hole14_id = update_course.hole14_id
        elif value == 20:
            existing_course.hole15_id = update_course.hole15_id
        elif value == 21:
            existing_course.hole16_id = update_course.hole16_id
        elif value == 22:
            existing_course.hole17_id = update_course.hole17_id
        elif value == 23:
            existing_course.hole18_id = update_course.hole18_id
        elif value == 24:
            existing_course.hole19_id = update_course.hole19_id
        elif value == 25:
            existing_course.hole20_id = update_course.hole20_id
        elif value == 26:
            existing_course.hole21_id = update_course.hole21_id
        elif value == 27:
            existing_course.hole22_id = update_course.hole22_id
        elif value == 28:
            existing_course.hole23_id = update_course.hole23_id
        elif value == 29:
            existing_course.hole24_id = update_course.hole24_id
        elif value == 30:
            existing_course.hole25_id = update_course.hole25_id
        elif value == 31:
            existing_course.hole26_id = update_course.hole26_id
        elif value == 32:
            existing_course.hole27_id = update_course.hole27_id
        elif value == 33:
            existing_course.hole28_id = update_course.hole28_id
        elif value == 34:
            existing_course.hole29_id = update_course.hole29_id
        elif value == 35:
            existing_course.hole30_id = update_course.hole30_id
        elif value == 36:
            existing_course.hole31_id = update_course.hole31_id
        elif value == 37:
            existing_course.hole32_id = update_course.hole32_id
        elif value == 38:
            existing_course.hole33_id = update_course.hole33_id
        elif value == 39:
            existing_course.hole34_id = update_course.hole34_id
        elif value == 40:
            existing_course.hole35_id = update_course.hole35_id
        elif value == 41:
            existing_course.hole36_id = update_course.hole36_id
        else:
            existing_course = update_course
    else:
        abort(
            404,
            f"Course with course name {course_id} not found"
        )

def update_length(course_id,course):
    existing_course = Course.query.filter(Course.id == course_id).one_or_none()
    if existing_course:
        update_course = course_schema.load(course, session=db_course.session)
        existing_course.length = update_course.length
        db_course.session.merge(existing_course)
        db_course.session.commit()
        return course_schema.dump(existing_course), 201
    else:
        abort(
            404,
            f"Course with course name {course_id} not found"
        )
def update(course_id, course):
    existing_course = Course.query.filter(Course.id == course_id).one_or_none()
    if existing_course:
        update_course = course_schema.load(course, session=db_course.session)
        existing_course.course_name = update_course.course_name
        existing_course.layout_name = update_course.layout_name
        existing_course.par = update_course.par
        existing_course.length = update_course.length
        existing_course.num_holes = update_course.num_holes
        existing_course.hole1_id = update_course.hole1_id
        existing_course.hole2_id = update_course.hole2_id
        existing_course.hole3_id = update_course.hole3_id
        existing_course.hole4_id = update_course.hole4_id
        existing_course.hole5_id = update_course.hole5_id
        existing_course.hole6_id = update_course.hole6_id
        existing_course.hole7_id = update_course.hole7_id
        existing_course.hole8_id = update_course.hole8_id
        existing_course.hole9_id = update_course.hole9_id
        existing_course.hole10_id = update_course.hole10_id
        existing_course.hole11_id = update_course.hole11_id
        existing_course.hole12_id = update_course.hole12_id
        existing_course.hole13_id = update_course.hole13_id
        existing_course.hole14_id = update_course.hole14_id
        existing_course.hole15_id = update_course.hole15_id
        existing_course.hole16_id = update_course.hole16_id
        existing_course.hole17_id = update_course.hole17_id
        existing_course.hole18_id = update_course.hole18_id
        existing_course.hole19_id = update_course.hole19_id
        existing_course.hole20_id = update_course.hole20_id
        existing_course.hole21_id = update_course.hole21_id
        existing_course.hole22_id = update_course.hole22_id
        existing_course.hole23_id = update_course.hole23_id
        existing_course.hole24_id = update_course.hole24_id
        existing_course.hole25_id = update_course.hole25_id
        existing_course.hole26_id = update_course.hole26_id
        existing_course.hole27_id = update_course.hole27_id
        existing_course.hole28_id = update_course.hole28_id
        existing_course.hole29_id = update_course.hole29_id
        existing_course.hole30_id = update_course.hole30_id
        existing_course.hole31_id = update_course.hole31_id
        existing_course.hole32_id = update_course.hole32_id
        existing_course.hole33_id = update_course.hole33_id
        existing_course.hole34_id = update_course.hole34_id
        existing_course.hole35_id = update_course.hole35_id
        existing_course.hole36_id = update_course.hole36_id
        db_course.session.merge(existing_course)
        db_course.session.commit()
        return course_schema.dump(existing_course), 201

    else:
        abort(
            404,
            f"Course with course name {course_id} not found"
        )

def delete(course_id):
    existing_course = Course.query.filter(Course.id == course_id).one_or_none()
    if existing_course:
        db_course.session.delete(existing_course)
        db_course.session.commit()
        return make_response(f"{course_id} successfully deleted", 200)
    else:
        abort(404,f"Course with course name {course_id} not found")
