import flask, flask.views
import os


class Main(flask.views.MethodView):
	def get(self, page="login"):
		if "username" in flask.session:
			page = "uploader"
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)