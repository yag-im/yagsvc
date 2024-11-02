import logging
import os

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from yagsvc.api import apispec
from yagsvc.api.account import bp as account_bp
from yagsvc.api.app import bp as app_bp
from yagsvc.api.auth import bp as auth_bp
from yagsvc.api.auth import discord_bp as auth_discord_bp
from yagsvc.api.auth import google_bp as auth_google_bp
from yagsvc.api.auth import login_manager
from yagsvc.api.auth import reddit_bp as auth_reddit_bp
from yagsvc.api.auth import twitch_bp as auth_twitch_bp
from yagsvc.api.misc import bp as misc_bp
from yagsvc.biz import (
    errors,
    log_handler,
)
from yagsvc.sqldb import sqldb

log = logging.getLogger("yagsvc")

BEHIND_PROXY = os.environ.get("BEHIND_PROXY", "false").lower() == "true"


def create_app() -> Flask:
    app = Flask(__name__, static_url_path="/api/static")
    app.config.from_prefixed_env()
    # composite config parameters
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f'postgresql://{os.environ["SQLDB_USERNAME"]}:{os.environ["SQLDB_PASSWORD"]}@{os.environ["SQLDB_HOST"]}:\
        {os.environ["SQLDB_PORT"]}/{os.environ["SQLDB_DBNAME"]}'
    )

    # initialize flask extensions
    login_manager.init_app(app)
    sqldb.init_app(app)
    errors.init_app(app)
    log_handler.init_app(app)

    if BEHIND_PROXY:
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)

    # register blueprints
    app.register_blueprint(account_bp)
    app.register_blueprint(app_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(auth_google_bp, url_prefix="/api/login")
    app.register_blueprint(auth_discord_bp, url_prefix="/api/login")
    app.register_blueprint(auth_reddit_bp, url_prefix="/api/login")
    app.register_blueprint(auth_twitch_bp, url_prefix="/api/login")
    app.register_blueprint(misc_bp)

    # this must come after blueprints registration
    apispec.init_app(app)

    # pylint: disable=pointless-string-statement
    """
    @app.before_request
    def log_request() -> None:
        log.info(request.__dict__)
        log.info(request.headers)
    """

    return app
