import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex_app_user = connexion.App(__name__, specification_dir=basedir)

app_user = connex_app_user.app
app_user.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'users.db'}"
app_user.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_user = SQLAlchemy(app_user)
ma_user = Marshmallow(app_user)