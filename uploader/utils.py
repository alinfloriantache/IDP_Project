import flask
import functools
import mysql.connector


def login_required(method):
	@functools.wraps(method)
	def wrapper(*args, **kwargs):
		if "username" in flask.session:
			return method(*args, **kwargs)
		else:
			flask.flash("A login is required to see the page!")
			return flask.redirect(flask.url_for("login"))
	return wrapper


def get_db_connection():
	config = {
        'user': 'root',
        'password': 'shortpass10',
        'host': 'database',
        'port': '3306',
        'database': 'music_app_db'
    }
	return connection = mysql.connector.connect(**config)