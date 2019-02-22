import requests
import logging
import sys
import jinja2
import os

from flask import Flask, render_template, send_file, current_app
from app.config import base_config, test_config
from app.database import db
from app.commands import create_db
from app.commands import populate_db
from app.commands import drop_db
from app.extensions import migrate
from app.extensions import bcrypt
from app.extensions import login_manager
from app.blueprints.user import user_blueprint
from app.blueprints.admin import admin_blueprint
from app.models.user import User
from app.repository.user_repository import UserRepository


def create_app(config=base_config):
    app = Flask(
        __name__, static_folder="..%s".format(current_app.config["DIST_DIR"])
    )
    app.config.from_object(config)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)

    register_blueprints(app)
    register_extensions(app)
    register_jinja_env(app)
    register_commands(app)

    @app.route("/")
    def index():
        dist_dir = current_app.config["DIST_DIR"]
        entry = os.path.join(dist_dir, "index.html")
        return send_file(entry)

    return app


def register_extensions(app):
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(user_blueprint, url_prefix="/user")
    app.register_blueprint(admin_blueprint, url_prefix="/admin")


def register_jinja_env(app):
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    my_loader = jinja2.ChoiceLoader(
        [
            jinja2.FileSystemLoader(
                [
                    os.path.join(PROJECT_ROOT, "static"),
                    os.path.join(PROJECT_ROOT, "templates"),
                ]
            ),
            app.jinja_loader,
        ]
    )
    app.jinja_loader = my_loader
    app.jinja_env.globals.update({"site_name": app.config["SITE_NAME"]})


def register_commands(app):
    for command in [create_db, populate_db, drop_db]:
        app.cli.command()(command)
