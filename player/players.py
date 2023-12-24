# users.py
from flask import abort, make_response
from config import db_player
from models import Player, players_schema, player_schema

def read_all():
    players = Player.query.all()
    return players_schema.dump(players)

def create(player):
    player_id = player.get("id")
    existing_player = Player.query.filter(Player.id == player_id).one_or_none()

    if existing_player is NONE:
        new_player = player_schema.load(player, session=db_player.session)
        db_player.session.add(new_player)
        db_player.session.commit()
        return player_schema.dump(new_player), 201
    else:
        abort(404 ,f"Player with id {player_id} already exists")

def read_one(player_id):
    player = Player.query.filter(Player.id == player_id).one_or_none()
    if player is not None:
        return player_schema.dump(player)
    else:
        abort(404, f"Player with id {player_id} not found")
        
def update(player_id, player):
    existing_player = Player.query.filter(Player.id == player_id).one_or_none()
    if existing_player:
        update_player = player_schema.load(player, session=db_player.session)
        existing_player.user_id = update_player.user_id
        existing_player.player_class = update_player.player_class
        existing_player.total_holes = update_player.total_holes
        existing_player.holes_played = update_player.holes_played
        existing_player.player_score = update_player.player_score
        existing_player.player_active = update_player.player_active
        existing_player.player_stars = update_player.player_stars
        db_player.session.merge(existing_player)
        db_player.session.commit()
        return player_schema.dump(existing_player), 201

    else:
        abort(
            404,
            f"Player with id {player_id} not found"
        )

def delete(player_id):
    existing_player = Player.query.filter(Player.id == player_id).one_or_none()
    if existing_player:
        db_player.session.delete(existing_player)
        db_player.session.commit()
        return make_response(f"{player_id} successfully deleted", 200)
    else:
        abort(404,f"Player with id {player_id} not found")
