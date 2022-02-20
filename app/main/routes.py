from flask import render_template, send_from_directory
from app.main import bp
from app.utils import url_for


@bp.route("/favicon.ico")
def favicon():
    return send_from_directory(
        url_for("static", filename="favicon.ico"),
        mimetype="image/vnd.microsoft.icon",
    )


@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
def index():
    return render_template("index.html", title="cnpryer.com")
