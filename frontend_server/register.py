import flask, flask.views
import utils


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
		passwd = flask.request.form["passwd"]

		conn = utils.get_db_connection()
		cursor = conn.cursor()
		cursor.execute("INSERT INTO users (username, password, uploader) VALUES (%s, %s, 0)", (username, passwd))
		conn.commit()
		conn.close()
		flask.flash("Account successfully created!")
		return flask.redirect(flask.url_for("login"))