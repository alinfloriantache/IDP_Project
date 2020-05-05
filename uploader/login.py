import flask, flask.views
import utils


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
		passwd = flask.request.form["passwd"]

		conn = utils.get_db_connection()
		cursor = conn.cursor()
		cursor.execute("SELECT username, password FROM users WHERE uploader = 1 AND username = %s", (username, ))
		result = cursor.fetchone()
		if result and result[1] == passwd:
			flask.session["username"] = username
		else:
			flask.flash("Username doesn't exist or incorrect password!")
			conn.close()
			return flask.redirect(flask.url_for("login"))
		conn.close()
		return flask.redirect(flask.url_for("uploader"))