import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex_app_hole = connexion.App(__name__, specification_dir=basedir)

app_hole = connex_app_hole.app
app_hole.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'holes.db'}"
app_hole.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_hole = SQLAlchemy(app_hole)
ma_hole = Marshmallow(app_hole)
