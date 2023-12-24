# users.py
from flask import abort, make_response
from config import db_encounter
from models import Encounter, encounters_schema, encounter_schema

def read_all():
    encounters = Encounter.query.all()
    return encounters_schema.dump(encounters)

def create(encounter):
    encounter_id = encounter.get("id")
    existing_encounter = Encounter.query.filter(Encounter.id == encounter_id).one_or_none()

    if existing_encounter is NONE:
        new_encounter = encounter_schema.load(encounter, session=db_encounter.session)
        db_encounter.session.add(new_encounter)
        db_encounter.session.commit()
        return encounter_schema.dump(new_encounter), 201
    else:
        abort(404 ,f"Encounter with id {encounter_id} already exists")

def read_one(encounter_id):
    encounter = Encounter.query.filter(Encounter.id == encounter_id).one_or_none()
    if encounter is not None:
        return encounter_schema.dump(encounter)
    else:
        abort(404, f"Encounter with id {encounter_id} not found")
        
def update(encounter_id, encounter):
    existing_encounter = Encounter.query.filter(Encounter.id == encounter_id).one_or_none()
    if existing_encounter:
        update_encounter = encounter_schema.load(encounter, session=db_encounter.session)
        existing_encounter.encounter_pool = update_encounter.encounter_pool
        existing_encounter.encounter_image = update_encounter.encounter_image
        existing_encounter.encounter_name = update_encounter.encounter_name
        existing_encounter.encounter_type = update_encounter.encounter_type
        existing_encounter.encounter_star = update_encounter.encounter_star
        existing_encounter.encounter_reward_code = update_encounter.encounter_reward_code
        db_encounter.session.merge(existing_encounter)
        db_encounter.session.commit()
        return encounter_schema.dump(existing_encounter), 201

    else:
        abort(
            404,
            f"Encounter with id {encounter_id} not found"
        )

def delete(encounter_id):
    existing_encounter = Encounter.query.filter(Encounter.id == encounter_id).one_or_none()
    if existing_encounter:
        db_encounter.session.delete(existing_encounter)
        db_encounter.session.commit()
        return make_response(f"{encounter_id} successfully deleted", 200)
    else:
        abort(404,f"Encounter with id {encounter_id} not found")
