# models.py

from config import db_dungeon
from config import ma_dungeon

class Dungeon(db_dungeon.Model):
    __tablename__ = "dungeon"
    id = db_dungeon.Column(db_dungeon.Integer, primary_key=True)
    dungeon_name = db_dungeon.Column(db_dungeon.String(32))
    dungeon_difficulty = db_dungeon.Column(db_dungeon.String(32))
    lvl_1 = db_dungeon.Column(db_dungeon.Integer)
    lvl_2 = db_dungeon.Column(db_dungeon.Integer)
    lvl_3 = db_dungeon.Column(db_dungeon.Integer)
    lvl_4 = db_dungeon.Column(db_dungeon.Integer)
    lvl_5 = db_dungeon.Column(db_dungeon.Integer)
    lvl_6 = db_dungeon.Column(db_dungeon.Integer)
    lvl_7 = db_dungeon.Column(db_dungeon.Integer)
    lvl_8 = db_dungeon.Column(db_dungeon.Integer)
    lvl_9 = db_dungeon.Column(db_dungeon.Integer)
    lvl_10 = db_dungeon.Column(db_dungeon.Integer)
    lvl_11 = db_dungeon.Column(db_dungeon.Integer)
    lvl_12 = db_dungeon.Column(db_dungeon.Integer)
    lvl_13 = db_dungeon.Column(db_dungeon.Integer)
    lvl_14 = db_dungeon.Column(db_dungeon.Integer)
    lvl_15 = db_dungeon.Column(db_dungeon.Integer)
    lvl_16 = db_dungeon.Column(db_dungeon.Integer)
    lvl_17 = db_dungeon.Column(db_dungeon.Integer)
    lvl_18 = db_dungeon.Column(db_dungeon.Integer)
    lvl_19 = db_dungeon.Column(db_dungeon.Integer)
    lvl_20 = db_dungeon.Column(db_dungeon.Integer)
    lvl_21 = db_dungeon.Column(db_dungeon.Integer)
    lvl_22 = db_dungeon.Column(db_dungeon.Integer)
    lvl_23 = db_dungeon.Column(db_dungeon.Integer)
    lvl_24 = db_dungeon.Column(db_dungeon.Integer)
    lvl_25 = db_dungeon.Column(db_dungeon.Integer)
    lvl_26 = db_dungeon.Column(db_dungeon.Integer)
    lvl_27 = db_dungeon.Column(db_dungeon.Integer)
    lvl_28 = db_dungeon.Column(db_dungeon.Integer)
    lvl_29 = db_dungeon.Column(db_dungeon.Integer)
    lvl_30 = db_dungeon.Column(db_dungeon.Integer)
    lvl_31 = db_dungeon.Column(db_dungeon.Integer)
    lvl_32 = db_dungeon.Column(db_dungeon.Integer)
    lvl_33 = db_dungeon.Column(db_dungeon.Integer)
    lvl_34 = db_dungeon.Column(db_dungeon.Integer)
    lvl_35 = db_dungeon.Column(db_dungeon.Integer)
    lvl_36 = db_dungeon.Column(db_dungeon.Integer)

class DungeonSchema(ma_dungeon.SQLAlchemyAutoSchema):
    class Meta:
        model = Dungeon
        load_instance = True
        sqla_session = db_dungeon.session
      
dungeon_schema = DungeonSchema()
dungeons_schema = DungeonSchema(many=True)