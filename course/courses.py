# users.py
from flask import abort, make_response
from config import db_course
from models import Course, courses_schema, course_schema

def read_all():
    courses = Course.query.all()
    return courses_schema.dump(courses)

def create(course):
    #This needs to be changed for course create
    course_name = course.get("course_name")
    existing_course = Course.query.filter(Course.course_name == course_name).one_or_none()

    if existing_course is None:
        new_course = course_schema.load(course, session=db_course.session)
        db_course.session.add(new_course)
        db_course.session.commit()
        return course_schema.dump(new_course), 201
    else:
        abort(404 ,f"Course with course name {course_name} already exists")

def read_one(course_id):
    #This needs to be changed to include a search for the layout name
    course = Course.query.filter(Course.id == course_id).one_or_none()
    if course is not None:
        return course_schema.dump(course)
    else:
        abort(404, f"Course with course name {course_id} not found")
        
def update(course_name, course):
    #This will need to change to be able to update courses
    existing_course = Course.query.filter(Course.course_name == course_name).one_or_none()
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
            f"Course with course name {course_name} not found"
        )

def delete(course_name):
    existing_course = Course.query.filter(Course.course_name == course_name).one_or_none()
    if existing_course:
        db_course.session.delete(existing_course)
        db_course.session.commit()
        return make_response(f"{course_name} successfully deleted", 200)
    else:
        abort(404,f"Course with course name {course_name} not found")
