# models.py

from config import db_game
from config import ma_game

class Game(db_game.Model):
    __tablename__ = "game"
    id = db_game.Column(db_game.Integer, primary_key=True)
    finished = db_game.Column(db_game.Integer)
    course_id = db_game.Column(db_game.Integer)
    game_mode = db_game.Column(db_game.Integer)
    date = db_game.Column(db_game.String(32))
    num_players = db_game.Column(db_game.Integer)
    player1_id = db_game.Column(db_game.Integer)
    player2_id = db_game.Column(db_game.Integer)
    player3_id = db_game.Column(db_game.Integer)
    player4_id = db_game.Column(db_game.Integer)
    player5_id = db_game.Column(db_game.Integer)
    player6_id = db_game.Column(db_game.Integer)
    player7_id = db_game.Column(db_game.Integer)
    player8_id = db_game.Column(db_game.Integer)
    
class GameSchema(ma_game.SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        load_instance = True
        sqla_session = db_game.session
     
game_schema = GameSchema()
games_schema = GameSchema(many=True)
