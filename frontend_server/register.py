import flask, flask.views
import requests


class Register(flask.views.MethodView):
	def get(self):
		return flask.render_template("register.html")

	def post(self):
		required = ["username", "passwd"]
		for r in required:
			if r not in flask.request.form:
				flask.flash("Error: {0} is required!".format(r))
				return flask.redirect(flask.url_for("register"))
		username = flask.request.form["username"]
		password = flask.request.form["passwd"]

		requests.post("http://backend_server:5000/register/", json={"username": username, "password": password})
		flask.flash("Account successfully created!")
		return flask.redirect(flask.url_for("login"))