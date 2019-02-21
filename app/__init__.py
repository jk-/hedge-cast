import requests
import logging
import sys

from flask import Flask, render_template
from app.config import base_config, test_config
from app.assets import assets
from app.database import db
from app.commands import create_db
from app.commands import populate_db
from app.extensions import migrate
from app.extensions import bcrypt
from app.extensions import login_manager
from app.blueprints.user import user_blueprint
from app.models.user import User
from app.repository.user_repository import UserRepository


def create_app(config=base_config):
    app = Flask(__name__)
    app.config.from_object(config)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)

    register_blueprints(app)
    register_extensions(app)
    register_jinja_env(app)
    register_commands(app)

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html.j2")

    @app.errorhandler(500)
    def error_500(error):
        return render_template("errors/500.html.j2"), error.code

    return app


def register_extensions(app):
    db.init_app(app)
    assets.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(user_blueprint, url_prefix="/user")


def register_jinja_env(app):
    app.jinja_env.globals.update({"site_name": app.config["SITE_NAME"]})


def register_commands(app):
    for command in [create_db, populate_db]:
        app.cli.command()(command)


def register_errorhandlers(app):
    def render_error(error):
        return render_template("errors/%s.html.j2" % error.code), error.code

    for error in [
        requests.codes.INTERNAL_SERVER_ERROR,
        requests.codes.NOT_FOUND,
        requests.codes.UNAUTHORIZED,
    ]:
        app.errorhandler(error)(render_error)
