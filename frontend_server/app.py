import flask, flask.views
import os
import requests

#Website Views
from main import Main
from login import Login
from register import Register
from music_library import MusicLibrary

app = flask.Flask(__name__)
app.secret_key = "most_secretKey_ever"
app.config["UPLOAD_FOLDER"] = "static/music"
app.config["MAX_CONTENT_PATH"] = 16 * 1024 * 1024

app.add_url_rule("/", view_func=Main.as_view("main"), methods=["GET"])
app.add_url_rule("/<page>/", view_func=Main.as_view("page"), methods=["GET"])
app.add_url_rule("/login/", view_func=Login.as_view("login"), methods=["GET", "POST"])
app.add_url_rule("/register/", view_func=Register.as_view("register"), methods=["GET", "POST"])
app.add_url_rule("/music_library/", view_func=MusicLibrary.as_view("music_library"), methods=["GET"])

@app.errorhandler(404)
def page_not_found(error):
	return flask.render_template('404.html'), 404


@app.route("/upload_song/", methods=["POST"])
def upload_song():
	f = flask.request.files["file"]
	path = os.path.join(flask.current_app.root_path, flask.current_app.config["UPLOAD_FOLDER"])
	if not os.path.isdir(path):
		os.makedirs(path)
	f.save(os.path.join(path, f.filename))
	return {}, 200


app.debug = True
app.run(host="0.0.0.0")