import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex_app_encounter = connexion.App(__name__, specification_dir=basedir)

app_encounter = connex_app_encounter.app
app_encounter.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'encounters.db'}"
app_encounter.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_encounter = SQLAlchemy(app_encounter)

ma_encounter = Marshmallow(app_encounter)