import flask, flask.views
import requests


class Login(flask.views.MethodView):
	def get(self):
		return flask.render_template("login.html")

	def post(self):
		if "logout" in flask.request.form:
			flask.session.pop("username", None)
			return flask.redirect(flask.url_for("login"))
		required = ["username", "passwd"]
		for r in required:
			if r not in flask.request.form:
				flask.flash("Error: {0} is required!".format(r))
				return flask.redirect(flask.url_for("login"))
		username = flask.request.form["username"]
		password = flask.request.form["passwd"]

		response = requests.get("http://backend_server:5000/validate_login/", json={"username": username, "password": password})
		if response.status_code == requests.codes.ok:
			flask.session["username"] = username
		else:
			flask.flash("Username doesn't exist or incorrect password!")
			return flask.redirect(flask.url_for("login"))
		return flask.redirect(flask.url_for("music_library"))