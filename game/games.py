# users.py
from flask import abort, make_response
from config import db_game
from models import Game, games_schema, game_schema

def read_all():
    games = Game.query.all()
    return games_schema.dump(games)

def create(game):
    game_id = game.get("id")
    existing_game = Game.query.filter(Game.id == game_id).one_or_none()

    if existing_game is NONE:
        new_game = game_schema.load(game, session=db_game.session)
        db_game.session.add(new_game)
        db_game.session.commit()
        return game_schema.dump(new_game), 201
    else:
        abort(404 ,f"Game with id {game_id} already exists")

def read_one(game_id):
    game = Game.query.filter(Game.id == game_id).one_or_none()
    if game is not None:
        return game_schema.dump(game)
    else:
        abort(404, f"Game with id {game_id} not found")
        
def update(game_id, game):
    existing_game = Game.query.filter(Game.id == game_id).one_or_none()
    if existing_game:
        update_game = game_schema.load(game, session=db_game.session)
        existing_game.finished = update_game.finished
        existing_game.course_id = update_game.course_id
        existing_game.game_mode = update_game.game_mode
        existing_game.date = update_game.date
        existing_game.num_players = update_game.num_players
        existing_game.player1_id = update_game.player1_id
        existing_game.player2_id = update_game.player2_id
        existing_game.player3_id = update_game.player3_id
        existing_game.player4_id = update_game.player4_id
        existing_game.player5_id = update_game.player5_id
        existing_game.player6_id = update_game.player6_id
        existing_game.player7_id = update_game.player7_id
        existing_game.player8_id = update_game.player8_id
        db_game.session.merge(existing_game)
        db_game.session.commit()
        return game_schema.dump(existing_game), 201

    else:
        abort(
            404,
            f"Game with id {game_id} not found"
        )

def delete(game_id):
    existing_game = Game.query.filter(Game.id == game_id).one_or_none()
    if existing_game:
        db_game.session.delete(existing_game)
        db_game.session.commit()
        return make_response(f"{game_id} successfully deleted", 200)
    else:
        abort(404,f"Game with id {game_id} not found")
