# flake8: noqa
from flask import Blueprint

bp = Blueprint("api", __name__)

from app.api import errors
