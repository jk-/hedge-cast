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
from app.commands import populate_category
from app.commands import populate_plans
from app.commands import populate_playlist
from app.commands import populate_videos
from app.commands import drop_db
from app.extensions import migrate
from app.extensions import bcrypt
from app.extensions import cors
from app.blueprints.auth import auth_blueprint
from app.blueprints.users import users_blueprint
from app.blueprints.plan import plan_blueprint
from app.blueprints.role import roles_blueprint
from app.blueprints.playlist import playlist_blueprint
from app.blueprints.videos import videos_blueprint
from app.blueprints.categories import category_blueprint
from app.models.user import User
from app.repository.user_repository import UserRepository


def create_app(config=base_config):
    app = Flask(__name__, static_folder="../dist")
    app.config.from_object(config)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)

    register_blueprints(app)
    register_extensions(app)
    register_jinja_env(app)
    register_commands(app)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def catch_all(path):
        dist_dir = current_app.config["DIST_DIR"]
        entry = os.path.join(dist_dir, "index.html")
        return send_file(entry)

    return app


def register_extensions(app):
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})


def register_blueprints(app):
    API_PATH = "/api"
    app.register_blueprint(auth_blueprint, url_prefix=API_PATH)
    app.register_blueprint(users_blueprint, url_prefix=API_PATH)
    app.register_blueprint(category_blueprint, url_prefix=API_PATH)
    app.register_blueprint(plan_blueprint, url_prefix=API_PATH)
    app.register_blueprint(playlist_blueprint, url_prefix=API_PATH)
    app.register_blueprint(roles_blueprint, url_prefix=API_PATH)
    app.register_blueprint(videos_blueprint, url_prefix=API_PATH)


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
    for command in [
        create_db,
        populate_db,
        drop_db,
        populate_category,
        populate_plans,
        populate_playlist,
        populate_videos,
    ]:
        app.cli.command()(command)
