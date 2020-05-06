import flask
import os
import utils
import requests

from werkzeug.utils import secure_filename


def is_mp3_file(filename):
	return '.' in filename and filename.split(".")[-1].lower() == "mp3"


class Uploader(flask.views.MethodView):
	@utils.login_required
	def get(self):
		return flask.render_template("uploader.html")

	@utils.login_required
	def post(self):
		f = flask.request.files["file"]
		if is_mp3_file(f.filename):
			path = os.path.join(flask.current_app.instance_path, flask.current_app.config["UPLOAD_FOLDER"])
			if not os.path.isdir(path):
				os.makedirs(path)
			f.save(os.path.join(path, secure_filename(f.filename)))
			conn = utils.get_db_connection()
			cursor = conn.cursor()
			cursor.execute("INSERT INTO songs (name) VALUES (%s)", (secure_filename(f.filename), ))
			conn.commit()
			conn.close()

			file = os.path.join(path, secure_filename(f.filename))
			files = {"file": open(file, 'rb')}
			response = requests.post("http://frontend_server:5000/upload_song/", files=files)

			flask.flash("File uploaded succesfully!")
		else:
			flask.flash("Format not supported!")
		return flask.redirect(flask.url_for("uploader"))