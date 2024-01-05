# models.py

from config import db_user
from config import ma_user

class User(db_user.Model):
    __tablename__ = "user"
    id = db_user.Column(db_user.Integer, primary_key=True)
    username = db_user.Column(db_user.String(32), unique=True)
    password = db_user.Column(db_user.String(32))
    phone_id = db_user.Column(db_user.String(32))
    games_played = db_user.Column(db_user.Integer)

class UserSchema(ma_user.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db_user.session
          
user_schema = UserSchema()
users_schema = UserSchema(many=True)