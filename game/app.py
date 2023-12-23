from flask import render_template

import config
from models import Game

app_game = config.connex_app_game
app_game.add_api(config.basedir / "swagger_game.yml")

@app_game.route("/")
def home():
	games = Game.query.all()
	return render_template("home_game.html", games=games)

if __name__ == "__main__":
 	app_game.run(host="0.0.0.0", port=8001, debug=True)
