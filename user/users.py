# users.py
from flask import abort, make_response
from config import db_user
from models import User, users_schema, user_schema

def read_all():
    users = User.query.all()
    return users_schema.dump(users)

def create(user):
    username = user.get("username")
    existing_user = User.query.filter(User.username == username).one_or_none()

    if existing_user is NONE:
        new_user = user_schema.load(user, session=db_user.session)
        db_user.session.add(new_user)
        db_user.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(404 ,f"User with username {username} already exists")

def read_one(username):
    user = User.query.filter(User.username == username).one_or_none()
    if user is not None:
        return user_schema.dump(user)
    else:
        abort(404, f"Person with username {username} not found")
        
def update(username, user):
    existing_user = User.query.filter(User.username == username).one_or_none()
    if existing_user:
        update_user = user_schema.load(user, session=db_user.session)
        existing_user.password = update_user.password
        db_user.session.merge(existing_user)
        db_user.session.commit()
        return user_schema.dump(existing_user), 201

    else:
        abort(
            404,
            f"Person with username {username} not found"
        )

def delete(username):
    existing_user = User.query.filter(User.username == username).one_or_none()
    if existing_user:
        db_user.session.delete(existing_user)
        db_user.session.commit()
        return make_response(f"{username} successfully deleted", 200)
    else:
        abort(404,f"User with username {username} not found")
