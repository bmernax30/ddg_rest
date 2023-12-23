from flask import render_template

import config
from models import User

app_user = config.connex_app_user
app_user.add_api(config.basedir / "swagger_user.yml")

@app_user.route("/")
def home():
	users = User.query.all()
	return render_template("home_user.html", users=users)


if __name__ == "__main__":
	app_user.run(host="0.0.0.0", port=8000, debug=True)