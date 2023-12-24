# users.py
from flask import abort, make_response
from config import db_hole
from models import Hole, holes_schema, hole_schema

def read_all():
    holes = Hole.query.all()
    return holes_schema.dump(holes)

def create(hole):
    hole_id = hole.get("id")
    existing_hole = Hole.query.filter(Hole.id == hole_id).one_or_none()

    if existing_hole is NONE:
        new_hole = hole_schema.load(hole, session=db_hole.session)
        db_hole.session.add(new_hole)
        db_hole.session.commit()
        return hole_schema.dump(new_hole), 201
    else:
        abort(404 ,f"Hole with id {hole} already exists")

def read_one(hole_id):
    hole = Hole.query.filter(Hole.id == hole_id).one_or_none()
    if hole is not None:
        return hole_schema.dump(hole)
    else:
        abort(404, f"Hole with id {hole_id} not found")
        
def update(hole_id, hole):
    existing_hole = Hole.query.filter(Hole.id == hole_id).one_or_none()
    if existing_hole:
        update_hole = hole_schema.load(hole, session=db_hole.session)
        existing_hole.course_id = update_hole.course_id
        existing_hole.hole_number = update_hole.hole_number
        existing_hole.hole_par = update_hole.hole_par
        existing_hole.hole_distance = update_hole.hole_distance
        db_hole.session.merge(existing_hole)
        db_hole.session.commit()
        return hole_schema.dump(existing_hole), 201

    else:
        abort(
            404,
            f"Hole with id {hole_id} not found"
        )

def delete(hole_id):
    existing_hole = Hole.query.filter(Hole.id == hole_id).one_or_none()
    if existing_hole:
        db_hole.session.delete(existing_hole)
        db_hole.session.commit()
        return make_response(f"{hole_id} successfully deleted", 200)
    else:
        abort(404,f"Hole with id {hole_id} not found")
