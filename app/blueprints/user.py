from flask import (
    Blueprint,
    render_template,
    abort,
    redirect,
    url_for,
    request,
    flash,
)
from jinja2 import TemplateNotFound
from flask_login import login_required, login_user, logout_user
from app.extensions import login_manager
from app.repository.user_repository import UserRepository
from app.models.user import User

user_blueprint = Blueprint("user", __name__, template_folder="templates")


@login_manager.user_loader
def load_user(user_id):
    return UserRepository.get_by_id(user_id)


@user_blueprint.route("/login")
def index():
    return render_template("user/login.html.j2")


@user_blueprint.route("/l", methods=["GET", "POST"])
def login():

    user = UserRepository.query.filter_by(
        username=request.form.get("username")
    ).first()

    if not user:
        flash("Invalid user", "error")
        return render_template("user/login.html.j2")

    if not user.check_password(request.form.get("password")):
        flash("Invalid password", "error")
        return render_template("user/login.html.j2")

    login_user(user)
    return redirect(url_for("index"))


@user_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
