from flask import render_template

import config
from models import HolePlayed

app_hole_played = config.connex_app_hole_played
app_hole_played.add_api(config.basedir / "swagger_hole_played.yml")

@app_hole_played.route("/")
def home():
	holes_played = HolePlayed.query.all()
	return render_template("home_hole_played.html", holes_played=holes_played)

if __name__ == "__main__":
 	app_hole_played.run(host="0.0.0.0", port=8003, debug=True)