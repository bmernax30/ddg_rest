import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex_app_hole_played = connexion.App(__name__, specification_dir=basedir)

app_hole_played = connex_app_hole_played.app
app_hole_played.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'holes_played.db'}"
app_hole_played.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_hole_played = SQLAlchemy(app_hole_played)
ma_hole_played = Marshmallow(app_hole_played)