import flask, flask.views
import os

#Website Views
from main import Main
from login import Login
from uploader import Uploader

app = flask.Flask(__name__)
app.secret_key = "most_secretKey_ever"
app.config["UPLOAD_FOLDER"] = "static/music"
app.config["MAX_CONTENT_PATH"] = 16 * 1024 * 1024

app.add_url_rule("/", view_func=Main.as_view("main"), methods=["GET"])
app.add_url_rule("/<page>/", view_func=Main.as_view("page"), methods=["GET"])
app.add_url_rule("/login/", view_func=Login.as_view("login"), methods=["GET", "POST"])
app.add_url_rule("/uploader/", view_func=Uploader.as_view("uploader"), methods=["GET", "POST"])

@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404


app.debug = True
app.run(host="0.0.0.0")