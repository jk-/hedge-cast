from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

login = Blueprint("login", __name__, template_folder="templates")


@login.route("/")
def index():
    return render_template("user/login.html.j2")
