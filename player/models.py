# models.py

from config import db_player
from config import ma_player

class Player(db_player.Model):
    __tablename__ = "player"
    id = db_player.Column(db_player.Integer, primary_key=True)
    local_id = db_player.Column(db_player.Integer)
    username = db_player.Column(db_player.String(32))
    player_class = db_player.Column(db_player.String(32))
    total_holes = db_player.Column(db_player.Integer)
    holes_played = db_player.Column(db_player.Integer)
    player_score = db_player.Column(db_player.Integer)
    player_active = db_player.Column(db_player.Integer)
    player_stars = db_player.Column(db_player.Integer)
    player_dungeon_level = db_player.Column(db_player.Integer)
    hole1_id = db_player.Column(db_player.Integer)
    hole2_id = db_player.Column(db_player.Integer)
    hole3_id = db_player.Column(db_player.Integer)
    hole4_id = db_player.Column(db_player.Integer)
    hole5_id = db_player.Column(db_player.Integer)
    hole6_id = db_player.Column(db_player.Integer)
    hole7_id = db_player.Column(db_player.Integer)
    hole8_id = db_player.Column(db_player.Integer)
    hole9_id = db_player.Column(db_player.Integer)
    hole10_id = db_player.Column(db_player.Integer)
    hole11_id = db_player.Column(db_player.Integer)
    hole12_id = db_player.Column(db_player.Integer)
    hole13_id = db_player.Column(db_player.Integer)
    hole14_id = db_player.Column(db_player.Integer)
    hole15_id = db_player.Column(db_player.Integer)
    hole16_id = db_player.Column(db_player.Integer)
    hole17_id = db_player.Column(db_player.Integer)
    hole18_id = db_player.Column(db_player.Integer)
    hole19_id = db_player.Column(db_player.Integer)
    hole20_id = db_player.Column(db_player.Integer)
    hole21_id = db_player.Column(db_player.Integer)
    hole22_id = db_player.Column(db_player.Integer)
    hole23_id = db_player.Column(db_player.Integer)
    hole24_id = db_player.Column(db_player.Integer)
    hole25_id = db_player.Column(db_player.Integer)
    hole26_id = db_player.Column(db_player.Integer)
    hole27_id = db_player.Column(db_player.Integer)
    hole28_id = db_player.Column(db_player.Integer)
    hole29_id = db_player.Column(db_player.Integer)
    hole30_id = db_player.Column(db_player.Integer)
    hole31_id = db_player.Column(db_player.Integer)
    hole32_id = db_player.Column(db_player.Integer)
    hole33_id = db_player.Column(db_player.Integer)
    hole34_id = db_player.Column(db_player.Integer)
    hole35_id = db_player.Column(db_player.Integer)
    hole36_id = db_player.Column(db_player.Integer)

class PlayerSchema(ma_player.SQLAlchemyAutoSchema):
    class Meta:
        model = Player
        load_instance = True
        sqla_session = db_player.session
   
player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)
