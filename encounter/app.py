from flask import render_template

import config
from models import Encounter

app_encounter = config.connex_app_encounter
app_encounter.add_api(config.basedir / "swagger_encounter.yml")

@app_encounter.route("/")
def home():
	encounters = Encounter.query.all()
	return render_template("home_encounter.html", encounters=encounters)


if __name__ == "__main__":
 	app_encounter.run(host="0.0.0.0", port=8006, debug=True)