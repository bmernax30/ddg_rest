import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex_app_game = connexion.App(__name__, specification_dir=basedir)

app_game = connex_app_game.app
app_game.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'games.db'}"
app_game.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_game = SQLAlchemy(app_game)
ma_game = Marshmallow(app_game)
