# users.py
from flask import abort, make_response
from config import db_dungeon
from models import Dungeon, dungeons_schema, dungeon_schema

def read_all():
    dungeons = Dungeon.query.all()
    return dungeons_schema.dump(dungeons)

def create(dungeon):
    dungeon_id = dungeon.get("id")
    existing_dungeon = Dungeon.query.filter(Dungeon.id == dungeon_id).one_or_none()

    if existing_dungeon is None:
        new_dungeon = dungeon_schema.load(dungeon, session=db_dungeon.session)
        db_dungeon.session.add(new_dungeon)
        db_dungeon.session.commit()
        return dungeon_schema.dump(new_dungeon), 201
    else:
        abort(404 ,f"Dungeon with id {dungeon_id} already exists")

def read_one(dungeon_id):
    dungeon = Dungeon.query.filter(Dungeon.id == dungeon_id).one_or_none()
    if dungeon is not None:
        return dungeon_schema.dump(dungeon)
    else:
        abort(404, f"Dungeon with id {dungeon_id} not found")
        
def update(dungeon_id, dungeon):
    existing_dungeon = Dungeon.query.filter(Dungeon.id == dungeon_id).one_or_none()
    if existing_dungeon:
        update_dungeon = dungeon_schema.load(dungeon, session=db_dungeon.session)
        existing_dungeon.dungeon_name = update_dungeon.dungeon_name
        existing_dungeon.dungeon_difficulty  = update_dungeon.dungeon_difficulty
        existing_dungeon.lvl_1 = update_dungeon.lvl_1
        existing_dungeon.lvl_2 = update_dungeon.lvl_2
        existing_dungeon.lvl_3 = update_dungeon.lvl_3
        existing_dungeon.lvl_4 = update_dungeon.lvl_4
        existing_dungeon.lvl_5 = update_dungeon.lvl_5
        existing_dungeon.lvl_6 = update_dungeon.lvl_6
        existing_dungeon.lvl_7 = update_dungeon.lvl_7
        existing_dungeon.lvl_8 = update_dungeon.lvl_8
        existing_dungeon.lvl_9 = update_dungeon.lvl_9
        existing_dungeon.lvl_10 = update_dungeon.lvl_10
        existing_dungeon.lvl_11 = update_dungeon.lvl_11
        existing_dungeon.lvl_12 = update_dungeon.lvl_12
        existing_dungeon.lvl_13 = update_dungeon.lvl_13
        existing_dungeon.lvl_14 = update_dungeon.lvl_14
        existing_dungeon.lvl_15 = update_dungeon.lvl_15
        existing_dungeon.lvl_16 = update_dungeon.lvl_16
        existing_dungeon.lvl_17 = update_dungeon.lvl_17
        existing_dungeon.lvl_18 = update_dungeon.lvl_18
        existing_dungeon.lvl_19 = update_dungeon.lvl_19
        existing_dungeon.lvl_20 = update_dungeon.lvl_20
        existing_dungeon.lvl_21 = update_dungeon.lvl_21
        existing_dungeon.lvl_22 = update_dungeon.lvl_22
        existing_dungeon.lvl_23 = update_dungeon.lvl_23
        existing_dungeon.lvl_24 = update_dungeon.lvl_24
        existing_dungeon.lvl_25 = update_dungeon.lvl_25
        existing_dungeon.lvl_26 = update_dungeon.lvl_26
        existing_dungeon.lvl_27 = update_dungeon.lvl_27
        existing_dungeon.lvl_28 = update_dungeon.lvl_28
        existing_dungeon.lvl_29 = update_dungeon.lvl_29
        existing_dungeon.lvl_30 = update_dungeon.lvl_30
        existing_dungeon.lvl_31 = update_dungeon.lvl_31
        existing_dungeon.lvl_32 = update_dungeon.lvl_32
        existing_dungeon.lvl_33 = update_dungeon.lvl_33
        existing_dungeon.lvl_34 = update_dungeon.lvl_34
        existing_dungeon.lvl_35 = update_dungeon.lvl_35
        existing_dungeon.lvl_36 = update_dungeon.lvl_36
        db_dungeon.session.merge(existing_dungeon)
        db_dungeon.session.commit()
        return dungeon_schema.dump(existing_dungeon), 201

    else:
        abort(
            404,
            f"Dungeon with id {dungeon_id} not found"
        )

def delete(dungeon_id):
    existing_dungeon = Dungeon.query.filter(Dungeon.id == dungeon_id).one_or_none()
    if existing_dungeon:
        db_dungeon.session.delete(existing_dungeon)
        db_dungeon.session.commit()
        return make_response(f"{dungeon_id} successfully deleted", 200)
    else:
        abort(404,f"Dungeon with id {dungeon_id} not found")
