from flask import render_template

import config
from models import Player

app_player = config.connex_app_player
app_player.add_api(config.basedir / "swagger_player.yml")

@app_player.route("/")
def home():
	players = Player.query.all()
	return render_template("home_player.html", players=players)

if __name__ == "__main__":
 	app_player.run(host="0.0.0.0", port=8004, debug=True)