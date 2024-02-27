# models.py

from config import db_encounter
from config import ma_encounter

class Encounter(db_encounter.Model):
    __tablename__ = "encounter"
    id = db_encounter.Column(db_encounter.Integer, primary_key=True)
    encounter_challenge = db_encounter.Column(db_encounter.String(32))
    encounter_description = db_encounter.Column(db_encounter.String(128))
    encounter_pool = db_encounter.Column(db_encounter.Integer)
    encounter_image = db_encounter.Column(db_encounter.String(32))
    encounter_name = db_encounter.Column(db_encounter.String(32))
    encounter_type = db_encounter.Column(db_encounter.Integer)
    encounter_star = db_encounter.Column(db_encounter.Integer)
    encounter_reward_code = db_encounter.Column(db_encounter.Integer)

class EncounterSchema(ma_encounter.SQLAlchemyAutoSchema):
    class Meta:
        model = Encounter
        load_instance = True
        sqla_session = db_encounter.session
      
encounter_schema = EncounterSchema()
encounters_schema = EncounterSchema(many=True)