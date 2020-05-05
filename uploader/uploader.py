import flask
import os
import utils

from werkzeug.utils import secure_filename


def is_mp3_file(filename):
	return '.' in filename and filename.split(".")[-1].lower() == "mp3"


class Uploader(flask.views.MethodView):
	@utils.login_required
	def get(self):
		songs = os.listdir("static/music")
		return flask.render_template("uploader.html", songs=songs)

	@utils.login_required
	def post(self):
		f = flask.request.files["file"]
		if is_mp3_file(f.filename):
			f.save(os.path.join(flask.current_app.config["UPLOAD_FOLDER"], secure_filename(f.filename)))
			flask.flash("File uploaded succesfully!")
		else:
			flask.flash("Format not supported!")
		return flask.redirect(flask.url_for("uploader"))