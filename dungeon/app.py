from flask import render_template

import config
from models import Dungeon

app_dungeon = config.connex_app_dungeon
app_dungeon.add_api(config.basedir / "swagger_dungeon.yml")

@app_dungeon.route("/")
def home():
	dungeons = Dungeon.query.all()
	return render_template("home_dungeon.html", dungeons=dungeons)


if __name__ == "__main__":
 	app_dungeon.run(host="0.0.0.0", port=8007, debug=True)