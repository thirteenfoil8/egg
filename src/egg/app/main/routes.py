from egg.app.main import bp
from flask import Flask, render_template, jsonify, request
from datetime import datetime
from egg.dao.web_counter import WebCounterDAO
from egg.models.models import WebCounter
from egg.app.ressources.index import get_counter


@bp.route('/')
def index():
    new_value, now = get_counter()
    return render_template('index.html', new_value=new_value,updated_at =now.strftime("%d, %b %Y at %H:%M:%S UTC"))