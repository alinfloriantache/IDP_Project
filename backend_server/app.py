import flask
import utils

app = flask.Flask(__name__)


@app.route("/validate_login/", methods=["GET"])
def validate_login():
	username = flask.request.json["username"]
	password = flask.request.json["password"]

	conn = utils.get_db_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT username, password FROM users WHERE uploader = 0 AND username = %s", (username, ))
	result = cursor.fetchone()
	conn.close()
	if result and result[1] == password:
		return {}, 200
	else:
		return {}, 401


@app.route("/music_library/", methods=["GET"])
def music_library():
	conn = utils.get_db_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT name FROM songs")
	result = cursor.fetchall()
	conn.close()
	return flask.jsonify(result)


app.debug = True
app.run(host="0.0.0.0")
