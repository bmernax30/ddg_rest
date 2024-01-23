# models.py

from config import db_hole_played
from config import ma_hole_played

class HolePlayed(db_hole_played.Model):
    __tablename__ = "hole_played"
    id = db_hole_played.Column(db_hole_played.Integer, primary_key=True)
    local_id = db_hole_played.Column(db_hole_played.Integer)
    hole_id = db_hole_played.Column(db_hole_played.Integer)
    strokes = db_hole_played.Column(db_hole_played.Integer)
    passive_used = db_hole_played.Column(db_hole_played.Integer)
    active_used = db_hole_played.Column(db_hole_played.Integer)
    encounter_id = db_hole_played.Column(db_hole_played.Integer)
    encounter_defeated = db_hole_played.Column(db_hole_played.Integer)
    hole_completed = db_hole_played.Column(db_hole_played.Integer)

class HolePlayedSchema(ma_hole_played.SQLAlchemyAutoSchema):
    class Meta:
        model = HolePlayed
        load_instance = True
        sqla_session = db_hole_played.session
    
hole_played_schema = HolePlayedSchema()
holes_played_schema = HolePlayedSchema(many=True)
