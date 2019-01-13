from flask import Blueprint

scpic = Blueprint('scpic', __name__)

from . import views
