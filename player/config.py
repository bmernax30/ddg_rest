import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex_app_player = connexion.App(__name__, specification_dir=basedir)

app_player = connex_app_player.app
app_player.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'players.db'}"
app_player.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_player = SQLAlchemy(app_player)
ma_player = Marshmallow(app_player)