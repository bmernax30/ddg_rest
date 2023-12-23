from flask import render_template

import config
from models import Hole

app_hole = config.connex_app_hole
app_hole.add_api(config.basedir / "swagger_hole.yml")


@app_hole.route("/")
def home():
	holes = Hole.query.all()
	return render_template("home_hole.html", holes=holes)


if __name__ == "__main__":
 	app_hole.run(host="0.0.0.0", port=8002, debug=True)