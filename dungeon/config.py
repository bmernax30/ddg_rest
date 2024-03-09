import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex_app_dungeon = connexion.App(__name__, specification_dir=basedir)

app_dungeon = connex_app_dungeon.app
app_dungeon.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'dungeons.db'}"
app_dungeon.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_dungeon = SQLAlchemy(app_dungeon)

ma_dungeon = Marshmallow(app_dungeon)