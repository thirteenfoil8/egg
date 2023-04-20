from flask import Blueprint

bp = Blueprint('main', __name__)

from egg.app.main import routes
