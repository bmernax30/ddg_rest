# models.py

from config import db_course
from config import ma_course
        
class Course(db_course.Model):
    __tablename__ = "course"
    id = db_course.Column(db_course.Integer, primary_key=True)
    course_name = db_course.Column(db_course.String(32))
    layout = db_course.Column(db_course.Integer)
    num_holes = db_course.Column(db_course.Integer)
    hole1_id = db_course.Column(db_course.Integer)
    hole2_id = db_course.Column(db_course.Integer)
    hole3_id = db_course.Column(db_course.Integer)
    hole4_id = db_course.Column(db_course.Integer)
    hole5_id = db_course.Column(db_course.Integer)
    hole6_id = db_course.Column(db_course.Integer)
    hole7_id = db_course.Column(db_course.Integer)
    hole8_id = db_course.Column(db_course.Integer)
    hole9_id = db_course.Column(db_course.Integer)
    hole10_id = db_course.Column(db_course.Integer)
    hole11_id = db_course.Column(db_course.Integer)
    hole12_id = db_course.Column(db_course.Integer)
    hole13_id = db_course.Column(db_course.Integer)
    hole14_id = db_course.Column(db_course.Integer)
    hole15_id = db_course.Column(db_course.Integer)
    hole16_id = db_course.Column(db_course.Integer)
    hole17_id = db_course.Column(db_course.Integer)
    hole18_id = db_course.Column(db_course.Integer)
    hole19_id = db_course.Column(db_course.Integer)
    hole20_id = db_course.Column(db_course.Integer)
    hole21_id = db_course.Column(db_course.Integer)
    hole22_id = db_course.Column(db_course.Integer)
    hole23_id = db_course.Column(db_course.Integer)
    hole24_id = db_course.Column(db_course.Integer)
    hole25_id = db_course.Column(db_course.Integer)
    hole26_id = db_course.Column(db_course.Integer)
    hole27_id = db_course.Column(db_course.Integer)
    hole28_id = db_course.Column(db_course.Integer)
    hole29_id = db_course.Column(db_course.Integer)
    hole30_id = db_course.Column(db_course.Integer)
    hole31_id = db_course.Column(db_course.Integer)
    hole32_id = db_course.Column(db_course.Integer)
    hole33_id = db_course.Column(db_course.Integer)
    hole34_id = db_course.Column(db_course.Integer)
    hole35_id = db_course.Column(db_course.Integer)
    hole36_id = db_course.Column(db_course.Integer)
    
class CourseSchema(ma_course.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        load_instance = True
        sqla_session = db_course.session
 
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)