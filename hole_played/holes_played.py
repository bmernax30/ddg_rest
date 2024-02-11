# users.py
from flask import abort, make_response
from config import db_hole_played
from models import HolePlayed, holes_played_schema, hole_played_schema

def read_all():

    holes_played = HolePlayed.query.all()
    return holes_played_schema.dump(holes_played)

def create(hole_played):
    hole_played_id = hole_played.get("id")
    existing_hole_played = HolePlayed.query.filter(HolePlayed.id == hole_played_id).one_or_none()

    if existing_hole_played is None:
        new_hole_played = hole_played_schema.load(hole_played, session=db_hole_played.session)
        db_hole_played.session.add(new_hole_played)
        db_hole_played.session.commit()
        return hole_played_schema.dump(new_hole_played), 201
    else:
        abort(404 ,f"Hole played with id {hole_played_id} already exists")

def read_one(hole_played_id):
    hole_played = HolePlayed.query.filter(HolePlayed.id == hole_played_id).one_or_none()
    if hole_played is not None:
        return hole_played_schema.dump(hole_played)
    else:
        abort(404, f"Hole played with id {hole_played_id} not found")
        
def update(hole_played_id, hole_played):
    existing_hole_played = HolePlayed.query.filter(HolePlayed.id == hole_played_id).one_or_none()
    if existing_hole_played:
        update_hole_played = hole_played_schema.load(hole_played, session=db_hole_played.session)
        existing_hole_played.local_id = update_hole_played.local_id
        existing_hole_played.hole_id = update_hole_played.hole_id
        existing_hole_played.strokes = update_hole_played.strokes
        existing_hole_played.passive_used = update_hole_played.passive_used
        existing_hole_played.active_used = update_hole_played.active_used
        existing_hole_played.encounter_id = update_hole_played.encounter_id
        existing_hole_played.encounter_defeated = update_hole_played.encounter_defeated
        existing_hole_played.hole_completed = update_hole_played.hole_completed
        db_hole_played.session.merge(existing_hole_played)
        db_hole_played.session.commit()
        return hole_played_schema.dump(existing_hole_played), 201

    else:
        abort(
            404,
            f"Hole played with id {hole_played_id} not found"
        )

def delete(hole_played_id):
    existing_hole_played = HolePlayed.query.filter(HolePlayed.id == hole_played_id).one_or_none()
    if existing_hole_played:
        db_hole_played.session.delete(existing_hole_played)
        db_hole_played.session.commit()
        return make_response(f"{hole_played_id} successfully deleted", 200)
    else:
        abort(404,f"Hole played with id {hole_played_id} not found")
