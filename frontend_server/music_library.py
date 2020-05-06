import flask
import os
import requests


class MusicLibrary(flask.views.MethodView):
	def get(self):
		songs = requests.get("http://backend_server:5000/music_library/")
		return flask.render_template("music_library.html", songs=songs.json())