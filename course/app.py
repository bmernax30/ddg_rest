from flask import render_template

import config
from models import Course

app_course = config.connex_app_course
app_course.add_api(config.basedir / "swagger_course.yml")

@app_course.route("/")
def home():
	courses = Course.query.all()
	return render_template("home_course.html", courses=courses)

if __name__ == "__main__":
 	app_course.run(host="0.0.0.0", port=8005, debug=True)