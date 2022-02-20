from flask import redirect, render_template, send_from_directory, flash
from app.main import bp
from app.utils import url_for
from app.constants import socials


@bp.route("/favicon.ico")
def favicon():
    return send_from_directory(
        url_for("static", filename="favicon.ico"),
        mimetype="image/vnd.microsoft.icon",
    )


@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
def index():
    flash(
        "Warning: On mobile devices the resume may look distorted. "
        "Use the dropdown link instead."
    )
    return render_template("index.html", title="cnpryer.com")


@bp.route("/github", methods=["GET"])
def github():
    return redirect(socials.GITHUB_URL)


@bp.route("/twitter", methods=["GET"])
def twitter():
    return redirect(socials.TWITTER_URL)


@bp.route("/instagram", methods=["GET"])
def instagram():
    return redirect(socials.INSTAGRAM_URL)


@bp.route("/devpost", methods=["GET"])
def devpost():
    return redirect(socials.DEVPOST_URL)


@bp.route("/medium", methods=["GET"])
def medium():
    return redirect(socials.MEDIUM_URL)


@bp.route("/linkedin", methods=["GET"])
def linkedin():
    return redirect(socials.LINKEDIN_URL)
