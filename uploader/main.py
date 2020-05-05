import flask, flask.views
import os


class Main(flask.views.MethodView):
	def get(self, page="login"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			songs = os.listdir("static/music")
			return flask.render_template(page, songs=songs)
		flask.abort(404)