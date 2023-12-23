# users.py
from flask import abort, make_response
from config import db_course
from models import Course, courses_schema, course_schema

def read_all():
    courses = Course.query.all()
    return courses_schema.dump(courses)

def create(course):
    course_name = course.get("course_name")
    existing_course = Course.query.filter(Course.course_name == course_name).one_or_none()

    if existing_course is NONE:
        new_course = course_schema.load(course, session=db_course.session)
        db_course.session.add(new_course)
        db_course.session.commit()
        return course_schema.dump(new_course), 201
    else:
        abort(404 ,f"Course with course name {course_name} already exists")

def read_one(course_name):
    course = Course.query.filter(Course.course_name == course_name).one_or_none()
    if course is not None:
        return course_schema.dump(course)
    else:
        abort(404, f"Course with course name {course_name} not found")
        
def update(course_name, course):
    existing_course = Course.query.filter(Course.course_name == course_name).one_or_none()
    if existing_course:
        update_course = course_schema.load(course, session=db_course.session)
        existing_course.password = update_course.password
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
