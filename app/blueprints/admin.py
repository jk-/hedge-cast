from flask import (
    Blueprint,
    render_template,
    abort,
    redirect,
    url_for,
    request,
    flash,
)
from flask_login import login_required
from app.repository.user_repository import UserRepository
from app.models.user import User
from app.roles_required import roles_required

admin_blueprint = Blueprint("admin", __name__, template_folder="templates")
