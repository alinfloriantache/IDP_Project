import flask
import os
import utils


class MusicLibrary(flask.views.MethodView):
	def get(self):
		songs = os.listdir("static/music")
		return flask.render_template("music_library.html", songs=songs)