import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex_app_course = connexion.App(__name__, specification_dir=basedir)

app_course = connex_app_course.app
app_course.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'courses.db'}"
app_course.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db_course = SQLAlchemy(app_course)
ma_course = Marshmallow(app_course)
