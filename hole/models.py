# models.py

from config import db_hole
from config import ma_hole

class Hole(db_hole.Model):
    __tablename__ = "hole"
    id = db_hole.Column(db_hole.Integer, primary_key=True)
    course_id = db_hole.Column(db_hole.Integer)
    hole_number = db_hole.Column(db_hole.Integer)
    hole_par = db_hole.Column(db_hole.Integer)
    hole_distance = db_hole.Column(db_hole.Integer)

class HoleSchema(ma_hole.SQLAlchemyAutoSchema):
    class Meta:
        model = Hole
        load_instance = True
        sqla_session = db_hole.session

hole_schema = HoleSchema()
holes_schema = HoleSchema(many=True)
