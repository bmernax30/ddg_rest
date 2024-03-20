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

    if existing_player is None:
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
        existing_player.local_id = update_player.local_id
        existing_player.username = update_player.username
        existing_player.player_class = update_player.player_class
        existing_player.total_holes = update_player.total_holes
        existing_player.holes_played = update_player.holes_played
        existing_player.player_score = update_player.player_score
        existing_player.player_active = update_player.player_active
        existing_player.player_stars = update_player.player_stars
        existing_player.player_dungeon_map = update_player.player_dungeon_map
        existing_player.player_dungeon_level = update_player.player_dungeon_level
        existing_player.hole1_id = update_player.hole1_id
        existing_player.hole2_id = update_player.hole2_id
        existing_player.hole3_id = update_player.hole3_id
        existing_player.hole4_id = update_player.hole4_id
        existing_player.hole5_id = update_player.hole5_id
        existing_player.hole6_id = update_player.hole6_id
        existing_player.hole7_id = update_player.hole7_id
        existing_player.hole8_id = update_player.hole8_id
        existing_player.hole9_id = update_player.hole9_id
        existing_player.hole10_id = update_player.hole10_id
        existing_player.hole11_id = update_player.hole11_id
        existing_player.hole12_id = update_player.hole12_id
        existing_player.hole13_id = update_player.hole13_id
        existing_player.hole14_id = update_player.hole14_id
        existing_player.hole15_id = update_player.hole15_id
        existing_player.hole16_id = update_player.hole16_id
        existing_player.hole17_id = update_player.hole17_id
        existing_player.hole18_id = update_player.hole18_id
        existing_player.hole19_id = update_player.hole19_id
        existing_player.hole20_id = update_player.hole20_id
        existing_player.hole21_id = update_player.hole21_id
        existing_player.hole22_id = update_player.hole22_id
        existing_player.hole23_id = update_player.hole23_id
        existing_player.hole24_id = update_player.hole24_id
        existing_player.hole25_id = update_player.hole25_id
        existing_player.hole26_id = update_player.hole26_id
        existing_player.hole27_id = update_player.hole27_id
        existing_player.hole28_id = update_player.hole28_id
        existing_player.hole29_id = update_player.hole29_id
        existing_player.hole30_id = update_player.hole30_id
        existing_player.hole31_id = update_player.hole31_id
        existing_player.hole32_id = update_player.hole32_id
        existing_player.hole33_id = update_player.hole33_id
        existing_player.hole34_id = update_player.hole34_id
        existing_player.hole35_id = update_player.hole35_id

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
