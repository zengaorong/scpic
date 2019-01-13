from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
photos = UploadSet('photos', IMAGES)


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__,static_folder='scpic', static_url_path='/scpic')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)


    from .program import scpic as scpic_blueprint
    app.register_blueprint(scpic_blueprint, url_prefix='/scpic')

    return app
